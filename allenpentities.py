import pandas as pd
import ast

# # using collections.OrderedDict.fromkeys()
# from collections import OrderedDict
# data=pd.read_csv(r"C:\Projects\ImageCarousel\static\allennlp_new.csv")
# entdata=data['entities']
# lists=entdata.apply(ast.literal_eval).to_list()
# cleaned_list=[]
# for i in lists:
#     new_list=[x.lower() for x in i]
#     new_list=list(set(new_list))
#     cleaned_list.append(new_list)
# sorted_list=[]    
# for i in cleaned_list:
#     l=sorted(i,key=len)
#     l.reverse()
#     sorted_list.append(l)
# answers=data['answer'].to_list()
# result=pd.DataFrame(columns=['answer','entities'])
# for index,answer in enumerate(answers):
#     new_result= pd.DataFrame({'answer':answer,'entities':[sorted_list[index]]})
#     result=pd.concat([result,new_result])
# print(result)
# result.to_csv(r"C:\Projects\ImageCarousel\static\allennlp_cleaned.csv")

def getallennlp():
    data=pd.read_csv(r'static/allennlp_results.csv')
    ent_data=data['allennlp_entities'][0]
    ext_ent_data=data['extracted_entities'][0]
    image_data=data['image_urls']
    image_lists=image_data.apply(ast.literal_eval).to_list()
    resultant_list=[]
    print(ent_data)
    print(ext_ent_data)
    for i in image_lists:
        new_list=[]
        for j in i:
           for k in j:
                new_list.append(k)
        resultant_list.append(new_list)
    print(resultant_list)

if __name__=='__main__':
    getallennlp()    