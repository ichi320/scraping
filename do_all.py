import do_align
import do_request
import files_utf8_to_cp932

def main():
    do_request.main()
    print('request finished.')
    do_align.main()
    print('align finished.')
    files_utf8_to_cp932.main()
    print('combert to cp932 finished.')


do_align.align_df()
if __name__ == '__main__':
    main()
