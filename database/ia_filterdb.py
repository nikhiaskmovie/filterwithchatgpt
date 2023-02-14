import base64
import logging
from struct import pack
import re
from pyrogram.file_id import FileId
from pymongo.errors import DuplicateKeyError
from umongo import Instance, Document, fields
from motor.motor_asyncio import AsyncIOMotorClient
from marshmallow.exceptions import ValidationError
from info import DATABASE_URI, DATABASE_NAME, COLLECTION_NAME, USE_CAPTION_FILTER
import datetime 
import requests
from bs4 import BeautifulSoup
import uuid

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


client = AsyncIOMotorClient(DATABASE_URI)
db = client[DATABASE_NAME]
instance = Instance.from_db(db)

@instance.register
class TextMessage(Document):
    post_link = fields.StrField(required=True)
    text = fields.StrField(required=True)
    message_text = fields.StrField(required=True)
    timestamp = fields.DateTimeField(default=datetime.now)

    class Meta:
        indexes = ('$text',)
        collection_name = COLLECTION_NAME

my_uuid = uuid.uuid4()
async def save_file(text, post_link):
    """Save text message in database"""

    # TODO: Find better way to get same message_id for same text to avoid duplicates
    message_id, message_ref = unpack_new_file_id(str(uuid.uuid4()))
    text = re.sub(r"(_|\-|\.|\+)", " ", text)
    try:
        message = TextMessage(
            message_id=message_id,
            text=text,
            post_link=post_link,
        )
    except ValidationError:
        logger.exception('Error occurred while saving text message in database')
        return False, 2
    else:
        try:
            await message.commit()
        except DuplicateKeyError:
            logger.warning(
                f'{text} is already saved in database'
            )

            return False, 0
        else:
            logger.info(f'{text} is saved to database')
            return True, 1


async def get_search_results(query, max_results=7, offset=0):
    """For given query return (results, next_offset)"""

    query = query.strip()

    if not query:
        raw_pattern = '.'
    elif ' ' not in query:
        raw_pattern = r'(\b|[\.\+\-_])' + query + r'(\b|[\.\+\-_])'
    else:
        raw_pattern = query.replace(' ', r'.*[\s\.\+\-_]')

    try:
        regex = re.compile(raw_pattern, flags=re.IGNORECASE)
    except:
        return []

    # Search the query in Google
    google_url = f'https://www.google.com/search?q={query}'
    google_response = requests.get(google_url)
    google_soup = BeautifulSoup(google_response.text, 'html.parser')
    search_results = google_soup.select('.tF2Cxc')

    # Extract relevant titles/keywords from search results
    titles = []
    for result in search_results:
        title = result.find('h3').get_text()
        titles.append(title)

    # Search the extracted titles/keywords in the database
    filter = {'$or': [{'text': {'$regex': keyword, '$options': 'i'}} for keyword in titles]}

    total_results = await TextMessage.count_documents(filter)
    next_offset = offset + max_results

    if next_offset > total_results:
        next_offset = ''

    cursor = TextMessage.find(filter)
    cursor.sort('$natural', -1)
    cursor.skip(offset).limit(max_results)
    messages = await cursor.to_list(length=max_results)

    return messages, next_offset, total_results





def unpack_new_file_id(new_file_id):
    """Return file_id, file_ref"""
    decoded = FileId.decode(new_file_id)
    file_id = encode_file_id(
        pack(
            "<iiqq",
            int(decoded.file_type),
            decoded.dc_id,
            decoded.media_id,
            decoded.access_hash
        )
    )
    file_ref = encode_file_ref(decoded.file_reference)
    return file_id, file_ref


async def get_file_details(query):
      filter = {'caption': query}
      filter = {'file_id': query}
      cursor = TextMessage.find(filter)
      ConnectionRefusedError = {'postlink': query}
      filedetails = await cursor.to_list(length=1)
      return filedetails

      
def encode_file_id(s: bytes) -> str:
    r = b""
    n = 0

    for i in s + bytes([22]) + bytes([4]):
        if i == 0:
            n += 1
        else:
            if n:
                r += b"\x00" + bytes([n])
                n = 0

            r += bytes([i])

    return base64.urlsafe_b64encode(r).decode().rstrip("=")

def encode_file_ref(file_ref: bytes) -> str:
    return base64.urlsafe_b64encode(file_ref).decode().rstrip("=")