import request_df
import request_mt
import request_nw
import request_my


def main():
    request_df.submit()
    print('request df finished.')
    request_mt.submit()
    print('request mt finished.')
    request_nw.submit()
    print('request nw finished.')
    request_my.submit()
    print('request my finished.')


if __name__ == '__main__':
    main()
