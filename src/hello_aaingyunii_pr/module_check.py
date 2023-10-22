def module_check():
    import importlib
    module_name_list = ["requests", "BeatifulSoup"]

    for i in module_name_list:
        if importlib.util.find_spec(i) is None:
            try:
                # 모듈 설치
                import pip
                pip.main(['install', i])
            except ImportError:
                print(f"{i} 패키지를 설치하는 데 실패했습니다. 수동으로 설치해주세요.")
        else:
            print(f"{i} 패키지는 이미 설치되어 있습니다.")