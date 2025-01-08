import yaml
import pickle
from flow_data import flow_1, flow_2, flow_3

flows: list = [flow_1, flow_2, flow_3]

# Fetching urls from all flows:
def fetch_url(flow): 
    api_data: dict = flow.get("api_data")
    if api_data:
        print(api_data.get('url'))  
    else: 
        print("No api_data found in the flow.")  

def fetch_main():
 print("Enter 1 to get url from flow_1")
 print("Enter 2 to get url from flow_2")
 print("Enter 3 to get url from flow_3")
 print("Enter 4 to get urls from all flows")
 flow_number = int(input("\nEnter 1, 2, 3 or 4: "))

 if flow_number == 1:  
    fetch_url(flow_1)          
 elif flow_number == 2:
    fetch_url(flow_2)
 elif flow_number == 3:
    fetch_url(flow_3)
 elif flow_number == 4:
    for flow in flows:  
        fetch_url(flow)  
 else:
    print("\nInvalid choice, please enter 1, 2, 3, or 4")
fetch_main()
  
    
#Add new entity
entity = input("\nEnter entity that you want to enter: ")
def set_entity(flow,entity):
      flow.get('entities').append(entity)  
      
def entity_main():
     print("\nEnter 1 to enter entity in flow_1")
     print("Enter 2 to enter entity in flow_2")
     print("Enter 3 to enter entity in flow_3")
     print("Enter 4 to enter entity in all")
     flow_entity = int(input("\nEnter 1, 2, 3 or 4: "))
     if flow_entity==1:         
          set_entity(flow_1, entity)
     elif flow_entity==2:
          set_entity(flow_2, entity)
     elif flow_entity==3:
          set_entity(flow_3, entity)
     elif flow_entity==4:
          for flow in flows:
           set_entity(flow, entity)
     else:
          print("\nInvalid choice, please enter 1, 2, 3, or 4")  
entity_main()

  
#Update new url
url=input("\nEnter new url: ")
def update_url(flow,url):
    flow.update({'url': url})
     
def url_main():
     print("\nEnter 1 to update url in flow_1")
     print("Enter 2 to update url in flow_2")
     print("Enter 3 to update url in flow_3")
     print("Enter 4 to update url in all")
     flow_entity = int(input("\nEnter 1, 2, 3 or 4: "))
     if flow_entity==1:         
          update_url(flow_1,url)    
     elif flow_entity==2:
          update_url(flow_2,url)    
     elif flow_entity==3:
          update_url(flow_3,url)    
     elif flow_entity==4:
          for flow in flows:
           update_url(flow,url)    
     else:
          print("\nInvalid choice, please enter 1, 2, 3, or 4") 
url_main()

#delete an entity from a flow
def delete_entity(flow):
    index = input("Enter index that you want to delete: ")
    if index.isdigit():
        index = int(index)  
        if 0 <= index < len(flow.get('entities', [])):  
            delete = flow['entities'].pop(index)  
            print(f"Deleted entity: {delete}")
        else:
            print("Index is out of range!")
    else:
        print("Please enter a valid integer index!")
        
def delete_entities():
    print("\nEnter 1 to delete entity from flow_1")
    print("Enter 2 to delete entity from flow_2")
    print("Enter 3 to delete entity from flow_3")
    print("Enter 4 to delete entity from all flows")
    
    delete_entity_flow = input("\nEnter 1, 2, 3 or 4: ")  
    if delete_entity_flow == '1':
        delete_entity(flow_1)
    elif delete_entity_flow == '2':
        delete_entity(flow_2)
    elif delete_entity_flow == '3':
        delete_entity(flow_3)
    elif delete_entity_flow == '4':
        for flow in flows:
            delete_entity(flow)
    else:
        print("\nInvalid choice, please enter 1, 2, 3, or 4.")
delete_entities()

# saving updated data in yaml and pickle file  
with open("updated_flows.yaml", "w") as yaml_file:
     yaml.dump(flows, yaml_file, default_flow_style=False)
print("# Data saved to YAML file.")


with open("updated_flows.pkl", "wb") as pickle_file:
     pickle.dump(flows, pickle_file)
print("# Data saved to Pickle file.")




    