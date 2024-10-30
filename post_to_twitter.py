import tweepy
import logging
import config
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Twitter client setup
client = tweepy.Client(
    bearer_token=config.BEARER_TOKEN,
    consumer_key=config.CONSUMER_KEY,
    consumer_secret=config.CONSUMER_SECRET,
    access_token=config.ACCESS_TOKEN,
    access_token_secret=config.ACCESS_SECRET
)

def post_to_twitter(text, audio_file):
    """
    Posts a thought as a caption with an attached audio file on Twitter.
    Args:
        text (str): The caption text.
        audio_file (str): Path to the MP3 file.
    Returns:
        bool: True if the post was successful, False otherwise.
    """
    try:
        media = client.media_upload(filename=audio_file)
        client.update_status(status=text, media_ids=[media.media_id])
        logging.info("Thought posted to Twitter successfully.")
        return True
    except tweepy.TweepyException as e:
        logging.error(f"Failed to post to Twitter: {e}")
        return False

if __name__ == "__main__":
    sample_text = "Eidos is pondering the future of human connection."
    post_success = post_to_twitter(sample_text, "eidos_thought.mp3")
    if post_success:
        print("Posted to Twitter successfully.")
    else:
        print("Failed to post on Twitter.")
