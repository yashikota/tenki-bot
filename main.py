import screenshot
import twitter


def main():
    img_path: str = screenshot.main()
    twitter.main(img_path)


if __name__ == "__main__":
    main()
