from celery import Celery
from celery.utils.log import get_task_logger
import feedparser
# import MySQLdb
from pprint import pprint
from celery.canvas import chain

app = Celery('tasks')
app.config_from_object('celeryconfig')

logger = get_task_logger(__name__)

@app.task
def add(x, y):
	logger.info("doing some work...")
	return "hello world"

@app.task
def parse_rss(uri):
	logger.info("parsing rss at uri " + uri)
	f = feedparser.parse(uri)
	return f

@app.task
def extract_data(parsed_feed):
# 	pp = pprint.PrettyPrinter(indent=4)
# 	file = open('data01', 'w')
# 	pp.pprint(parsedFeed, stream=file)
# 	with open('output.txt', 'wt') as out:
# 		pprint(parsedFeed, stream=out)
	items = dict()
	entries = parsed_feed['entries']
	for entry in entries:
		item_id = entry['vertis_id']
		item = dict()
		items[item_id] = item
		
		item['id'] = item_id
		item['title'] = get_value(entry, 'title')
		item['price'] = get_value(entry, 'vertis_price')
		item['s_date'] = get_value(entry, 'vertis_psdate')
		item['e_date'] = get_value(entry, 'vertis_edate')
		item['ctgry'] = get_value(entry, 'vertis_category2')
		item['link'] = get_value(entry, 'link')
	
	return items	
# 	pprint(items)	

def get_value(dictionary, key):
	if key in dictionary:
		return dictionary[key]
	return None
	
@app.task
def persist_data(items):
	
	
@app.task
def crawl_xml(merchant_name, location):
	uri = get_rss_feed_uri(merchant_name, location)
	chain(parse_rss(uri).s(), extract_data.s(), persist_data.s())

# TODO
def get_rss_feed_uri(merchant_name, location):
	return "https://pathmark.inserts2online.com/rss.jsp?drpStoreID=624";

def main():
	url = get_rss_feed_uri("PathMark", 11214);
	parsedFeed = parse_rss(url);
	items = extract_data(parsedFeed);
	persist_data(items);
	
if __name__ == "__main__":
	main()