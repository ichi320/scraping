import do_align
import do_request
import files_utf8_to_cp932

def main():
    do_request.main()
    do_align.main()
    files_utf8_to_cp932.main()



do_align.align_df()
if __name__ == '__main__':
    main()
