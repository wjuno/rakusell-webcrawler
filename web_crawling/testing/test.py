  

def test():
	str1 = "ab"
	DESC = "a"
	DESC2 = "b"
	DESC3 = "c"
	DESC4 = "d"


	
	RAW_DESC =  DESC in str1 if DESC else None 
	RAW_DESC2 = DESC2 in str1 if DESC else None
	RAW_DESC3 = DESC3 in str1 if DESC else None
	RAW_DESC4 = DESC4 in str1 if DESC else None


	DESC = ' '.join(''.join(DESC).split()) if RAW_DESC else None 
	DESC2 = ' '.join(''.join(DESC2).split()) if RAW_DESC2 else None 
	DESC3 = ' '.join(''.join(DESC3).split()) if RAW_DESC3 else None 
	DESC4 = ' '.join(''.join(DESC4).split()) if RAW_DESC4 else None 



	DESC_ARR = [DESC,DESC2,DESC3,DESC4]
	print(DESC_ARR)
	

	if DESC_ARR:
		DESC = ' || '.join(filter(None,DESC_ARR))

	if all(ele is None for ele in DESC_ARR) :
		DESC = 'no description'

	print(len(DESC_ARR))
	print('Total String is ====> ' + DESC)

if __name__ == "__main__":
	test()