import pandas as pd
import ast

# # using collections.OrderedDict.fromkeys()
# from collections import OrderedDict
def sortentities():
    data=pd.read_csv(r"C:\Projects\ImageCarousel\static\allennlp_line_ent.csv")
    entdata=data['entities']
    lists=entdata.apply(ast.literal_eval).to_list()
    cleaned_list=[]
    for i in lists:
        new_list=[x.lower() for x in i]
        new_list=list(set(new_list))
        cleaned_list.append(new_list)
    sorted_list=[]    
    for i in cleaned_list:
        l=sorted(i,key=len)
        l.reverse()
        sorted_list.append(l)
    answers=data['answer'].to_list()
    result=pd.DataFrame(columns=['answer','entities'])
    for index,answer in enumerate(answers):
        new_result= pd.DataFrame({'answer':answer,'entities':[sorted_list[index]]})
        result=pd.concat([result,new_result])
    print(result)
    result.to_csv(r"C:\Projects\ImageCarousel\static\allennlp_np_cleaned.csv")
    

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

def cleanentities():
    # sortentities()
    result=pd.read_csv(r'static/allennlp_line_ent.csv')
    black_list=['It','it','They','they','us','The','the','that','That','this','This','There','there','their'
                ,'Their','Them','them','we','1 .','2 .','3 .','4 .','5 .','6 .','7 .','8 .','9 .','10 .']
    entdata=result['entities']
    answers=result['answer'].to_list()
    ent_list=entdata.apply(ast.literal_eval).to_list()
    print(ent_list)
    cleaned_df=pd.DataFrame(columns=['answer','entities'])
    for index,entities in enumerate(ent_list):
        new_entities=[]
        for ent in entities:
            if ent in black_list or len(ent)<=2:
               continue
            else:
                new_entities.append(ent)
        new_df=pd.DataFrame({'answer':answers[index],'entities':[new_entities]})
        cleaned_df=pd.concat([cleaned_df,new_df])
        print(new_df)
    cleaned_df.to_csv(r'static/allennlp_np_new.csv') 

def sortnewentities():
        data=pd.read_csv(r'static/allennlp_np_new.csv')
        ent_data=data['entities']   
        answers=data['answer'].to_list()
        ent_list=ent_data.apply(ast.literal_eval).to_list()
        result=pd.DataFrame(columns=['answer','entities'])
        for index,ent in enumerate(ent_list):
            ent.reverse()
            new_result=pd.DataFrame({'answer':answers[index],'entities':[ent]})
            result=pd.concat([result,new_result])

        result.to_csv(r"static/allennlp_np_final.csv")    
            
        
if __name__=='__main__':
    cleanentities()