# main.py
from Scrapper.YoutubeScraper import YouTubeScraper
from Utils.filehandler import FileHandler

def main(video_url, output_file):
    # Initialize YouTubeScraper
    scraper = YouTubeScraper()
    scraper.open_video(video_url)
    
    # Load comments
    scraper.scroll_to_load_comments()
    usernames, comments = scraper.get_comments()
    
    # Save to CSV
    file_handler = FileHandler(output_file)
    file_handler.save_to_csv(usernames, comments)
    
    # Close the browser
    scraper.close_driver()

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_file = 'youtube_comments.csv'
    main(video_url, output_file)
