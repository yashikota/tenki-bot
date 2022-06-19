import screenshot as ss
import twitter


def main():
    img_path: str = ss.Screenshot().main()
    print("image path: {}".format(img_path))
    twitter.tweet(img_path)


if __name__ == "__main__":
    main()
