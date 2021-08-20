import os 

def main():
    print("--------------------------------------------------------------------")
    i = 1
    path = input("\nEnter The Path of Your files (example: C:/Users/yasin/Documents/test): ") + '/'
    file_name = input("What is Name Your File To Change (example: Yasin): ")
    format_file = input("What is your Format File (example: .pdf or .png): " )
    for name in os.listdir(path):
        new_name = file_name + str(i) + format_file
        source = path + name
        new_source = path + new_name
        os.rename(source,new_source)
        i += 1
        print("\n--File Change Successfully--")

        print("--------------------------------------------------------------------")
    input()

if  __name__ == '__main__':
    main()

# Made By Yasin Rezvani     