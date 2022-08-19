myList = [
	{
		'foo':12,
		'bar':14
	},
	{
		'moo':52,
		'car':641
	},
	{
		'doo':6,
		'tar':84
	}
]

myList.append({'joo':48, 'par':28})

print(myList)

myList[0]['bar'] = 52

myList[1]['gar'] = 38

del myList[2]['doo']

print(myList)