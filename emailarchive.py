import os
import shutil

def archive_email(src, dst):
    # Create the destination folder if it does not exist
    if not os.path.exists(dst):
        os.makedirs(dst)

    # Iterate through all the files in the source folder
    for filename in os.listdir(src):
        # Check if the file is an email
        if filename.endswith(".eml"):
            src_file = os.path.join(src, filename)
            dst_file = os.path.join(dst, filename)

            # Move the email file to the destination folder
            shutil.move(src_file, dst_file)

if __name__ == "__main__":
    src = "./inbox"
    dst = "./archive"
    archive_email(src, dst)
