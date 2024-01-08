from pytube import YouTube
import yaml


def download_video(url, output_path):
    try:
        yt = YouTube(url)
        print(f'[*] Downloading video: "{yt.title}"')

        yt.streams.get_highest_resolution().download(output_path)
        print(f"[DONE] Video downloaded succesfully!")

    except Exception as e:
        print(f"Could not download the video: {str(e)}")


def main():
    url = input("[INPUT] Insert the URL of the YouTube video: ")

    with open("config.yml", "r") as file:
        config = yaml.safe_load(file)
        try:
            output_path = config.get('output_path', '.')
        except:
            pass

    print(f"[INFO] The video will be downloaded into {output_path}")
    download_video(url, output_path)


if __name__ == "__main__":
    main()
