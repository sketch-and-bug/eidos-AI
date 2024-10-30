import schedule
import time
from generate_thoughts import generate_thought
from text_to_speech import text_to_speech
from post_to_twitter import post_to_twitter
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def eidos_daily_post():
    """
    Orchestrates the generation, conversion, and posting of Eidos's daily thought.
    """
    logging.info("Starting daily Eidos post sequence.")
    
    thought = generate_thought()
    if thought:
        audio_success = text_to_speech(thought, "eidos_daily_thought.mp3")
        if audio_success:
            post_success = post_to_twitter(thought, "eidos_daily_thought.mp3")
            if post_success:
                logging.info("Daily post completed successfully.")
            else:
                logging.warning("Failed to post thought on Twitter.")
        else:
            logging.warning("Failed to convert thought to audio.")
    else:
        logging.warning("Failed to generate thought.")

# Schedule Eidos to post once daily at a specific time
schedule.every().day.at("10:00").do(eidos_daily_post)

# Run the scheduler
if __name__ == "__main__":
    logging.info("Eidos Scheduler started.")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Run every 60 seconds to keep checking for pending tasks
