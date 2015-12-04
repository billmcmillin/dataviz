#adapted from https://gist.github.com/phillipjohnson/8889618
#as part of the tutorial on http://letstalkdata.com/2014/02/how-to-use-the-yelp-api-in-python/
import rauth
import time
import json
import unicodecsv
import re
import ast

from hide import hide

f = unicodecsv.writer(open("test.csv", "wb+"))

def main():
	locations = [45202, 45203, 45204, 45205, 45206, 45207, 45208, 45209, 45211, 45212, 45213,
	            45214, 45215, 45216, 45217, 45219, 45220, 45221, 45223, 45224, 45225, 45226,
	            45227, 45228, 45229, 45230, 45231, 45232, 45233, 45237, 45238, 45239]
	      
	api_calls = []
	
	for zip in locations:
		offset = 0
		while (offset < 200):
			params = get_search_parameters(zip, offset)
			offset = offset + 20
			api_calls.append(get_results(params))
		#Be a good internet citizen and rate-limit yourself
			time.sleep(1.0)
	'''
	with open('hide/data.json') as data_file:
		api_calls = eval(data_file.read())
	'''

	q = open("data.text","w")
	for item in api_calls:
		q.write(str(item))	#outfile.write(api_calls)

	row = ['','','','','','','','','','','','','']
	print api_calls
	#unpack the data
	for location in api_calls:
		for business in location['businesses']:
			row[0] = business['name']
			if 'address' in business['location']:
				address = business['location']['address']
				if address:
					addy = (address[0].encode('utf-8').strip())
					row[1] = get_address_value(addy)
			else:
				row[1] = ''
			if 'postal_code' in business['location']:
				row[2] = business['location']['postal_code']
			else:
				row[2] = ''
			if 'neighborhoods' in business['location']:
				neighborhood = business['location']['neighborhoods']
				nabe = neighborhood[0].encode('utf-8').strip()
				row[3] = get_simple_value(nabe)
			else:
				row[3] = ''
			row[4] = business['location']['coordinate']['latitude']
			row[5] = business['location']['coordinate']['longitude']
			row[6] = business['rating']
			row[7] = business['review_count']
			#row[8] = business['snippet']
			counter = 0
			if 'categories' in business:
				for item in business['categories']:
					cat = get_value(item)
					row[8 + counter] = cat
					counter = counter + 1
			if 'image_url' in business:
				img = business['image_url']
				row[11] = img
			else:
				row[11] = ''
			if 'url' in business:
				url = business['url']
				row[12] = url
			else:
				row[12] = ''
			f.writerow(row)
			

		 
def get_value(input):
	s = str(input)				
	start = 'u\''
	end = '\','
	result = re.search('%s(.*)%s' % (start, end), s).group(1)
	return result

def get_address_value(input):
	if input:
		result = input.split('\'', 1)[-1]
		result = result.upper()
		if result:
			return result

def get_simple_value(input):
	if input:
		result = input.split('\'', 1)[-1]
		if result:
			return result
			#print result
	

def get_search_parameters(zip, offset):
  #See the Yelp API for more details
  params = {}
  params["term"] = "restaurant"
  #params["ll"] = "{},{}".format(str(lat),str(long))
  params["location"] = zip
  params["radius_filter"] = "5000"
  params["limit"] = "20"
  params["offset"] = offset
 
  return params

def get_results(params):
 
  #Obtain these from Yelp's manage access page
  consumer_key = hide.My_Consumer_Key
  consumer_secret = hide.My_Consumer_Secret
  token = hide.My_Token
  token_secret = hide.My_Token_Secret
   
  session = rauth.OAuth1Session(
    consumer_key = consumer_key
    ,consumer_secret = consumer_secret
    ,access_token = token
    ,access_token_secret = token_secret)
     
  request = session.get("http://api.yelp.com/v2/search",params=params)
  print params
  print request

  #Transforms the JSON API response into a Python dictionary
  data = request.json()

  session.close()
   
  return data

if __name__=="__main__":
	main()
