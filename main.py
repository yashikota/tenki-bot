import screenshot as ss
import twitter as tw


def main():
    img_path: str = ss.Screenshot().main()
    print("image path: {}".format(img_path))
    tw.Twitter().tweet(img_path)


if __name__ == "__main__":
    main()
