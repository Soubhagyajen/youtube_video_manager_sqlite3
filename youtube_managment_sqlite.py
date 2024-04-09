import sqlite3
con = sqlite3.connect("youtube_video.db")
cor= con.cursor()
cor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
''')

def list_videos():
    print("\n")
    print("*"*70)
    cor.execute("SELECT * FROM videos")
    for row in cor.fetchall():
        print(row)
    print("\n")
    print("*"*70)    

def add_videos(name,time):
    cor.execute("INSERT INTO videos (name,time) values(?,?)",(name,time))
    con.commit()
     

def update_videos(video_id,new_name,new_time):
     cor.execute("UPDATE videos SET name =?, time =? WHERE id = ?" ,(new_name,new_time,video_id))
     con.commit()

def delete_videos(video_id):
    cor.execute("DELETE FROM videos WHERE id =?" , (video_id,))
    con.commit()
  
def main():

    while True:

        print("Welcome to youtube video manager .|| Enter your choice :")
        print("1. List videos")
        print("2. add videos")
        print("3. update videos")
        print("4. delete videos")
        print("5. Exit the app")
        choice=input("enter your choice : ")
        if (choice == '1'):
            list_videos()
        elif (choice =='2'):
            name=input("enter the youtube video name : ")
            time=input("enter the youtube video time : ")
            add_videos(name,time)
        elif (choice == '3'):
            video_id=input("enter the video id to update: ")
            name=input("enter the name to update :")
            time=input("enter the time to update: ")
            update_videos(video_id,name,time)
        elif (choice=='4'):
            video_id=input("enter the video id to delete video ")
            delete_videos(video_id)
        elif (choice == '5'):
            break
        else: 
            print("invalid choice !!!")           


    con.close()        



if __name__ == "__main__" :
    main()