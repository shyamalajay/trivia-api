import os
import random
from pyairtable import Table
from dotenv import load_dotenv

load_dotenv()

table = Table(
    os.getenv("AIRTABLE_API_KEY"),
    os.getenv("AIRTABLE_BASE_ID"),
    os.getenv("AIRTABLE_TABLE_NAME")
)

def get_random_fact(category=None):
    if category:
        records = table.all(
            formula=f"{{category}} = '{category}'"
        )
    else:
        records = table.all()

    if not records:
        return None

    record = random.choice(records)
    fields = record["fields"]

    return {
        "id": record["id"],
        "fact": fields.get("fact"),
        "category": fields.get("category")
    }
