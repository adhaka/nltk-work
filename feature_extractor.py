from preprocess import process
import nltk

def feature_extraction():
	url_crime_list = ["http://www.indianexpress.com/news/odisha-woman-courted-through-sms-raped-thrown-from-car/1141423/",
	"http://www.indianexpress.com/news/up-shocker-girl-allegedly-gangraped-set-afire-in-etawah/1141014/", 
	"http://www.indianexpress.com/news/up-relatives-of-accused-chop-off-gangrape-victims-tongue/1140769/",
	"http://www.indianexpress.com/news/doctor-rapes-girl-on-pretext-of-marriage-makes-obscene-mms/1140525/",
	"http://www.indianexpress.com/news/goa-nine-human-skeletons-found-in-pit-police-suspect-murder/1138479/",
	"http://www.indianexpress.com/news/missing-eightyearold-girl-s-body-found-in-neighbour-s-sink/1138466/",
	"http://www.indianexpress.com/news/excorporator-from-maharashtra-booked-for-cheating-and-raping-marathi-actress/1138323/",
	"http://www.indianexpress.com/news/kashmir-youth-arrested-for-raping-minor-circulating-mms/1137697/", 
	"http://www.indianexpress.com/news/minor-girl-raped-killed-in-arunachal/1137118/",
	"http://www.indianexpress.com/news/man-rapes-niece-in-manipur/1137111/",
	"http://www.indianexpress.com/news/maoist-attack-in-jharkhand-leaves-five-cops-including-pakur-sp-balihar-dead/1136691/",
	"http://www.indianexpress.com/news/kashmir-2-youths-killed-in-alleged-army-firing-in-bandipora-trigger-protests/1135820/",
	"http://www.indianexpress.com/news/us-woman-roommate-allegedly-raped-by-landlord-during-power-cut-in-south-delhi/1133806/",
	"http://www.indianexpress.com/news/pune-techie-held-for-raping-domestic-help/1134400/",
	"http://www.indianexpress.com/news/man-kills-pregnant-daughter-for-marrying-out-of-caste/1135112/",
	"http://www.indianexpress.com/news/gurgaon-rape-main-accused-arrested/1135489/",
	"http://www.indianexpress.com/news/bsp-leader-murder-son-hatched-plot-to-kill-deepak-bhardwaj-says-chargesheet/1135339/",
	"http://www.indianexpress.com/news/kashmir-man-sets-son-on-fire-attempts-suicide/1135578/",
	"http://www.indianexpress.com/news/kashmir-6-persons-killed-in-firing-in-ramban-district-shinde-orders-probe/1143542/"]
	
	url_non_crime_list = ["http://www.indianexpress.com/news/heavy-rains-throw-traffic-out-of-gear-in-delhi-cause-massive-waterlogging/1144422/", \
		"http://www.indianexpress.com/news/wayne-rooney-an-outsider-at-manchester-united/1144275/",
		"http://www.indianexpress.com/news/people-wave-at-saturn-mercury-as-nasa-spacecraft-takes-pictures/1144391/",
		"http://www.indianexpress.com/news/bhaag-milka-bhaag-goes-taxfree-in-maharashtra/1144435/", 
		"http://www.indianexpress.com/news/narendra-modi-gets-a-grip-on-bjp-leadership/1144315/", 
		"http://www.indianexpress.com/news/brace-for-tough-year-growth-to-slow-pm/1144310/", 
		"http://www.indianexpress.com/news/congress-slams-rajnath-singhs-english-language-remark/1144206/", 
		"http://www.indianexpress.com/news/john-kerry-talked-to-venezuela-about-snowden-us/"]
 
	words = process(url_crime_list)
	non_crime_words = process(url_non_crime_list)
	crime_words = []
	for word in words:
		if word not in non_crime_words:
			crime_words.append(word)
				
	
	print len(crime_words)
	fd = nltk.FreqDist(crime_words)
	key_features = []
	key_features = [word for word, count in fd.items() if count > 2]
	key_features_types = nltk.pos_tag(key_features)
	key_features_nouns = [word for word, type in key_features_types if type == 'NN']
	
	fd.tabulate() 
	
 
 '''def isPresentInNonCrimeWords(word):
	return word not in '''