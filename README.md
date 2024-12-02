Sau khi clone repo về, đi vào thư mục bluequant-sim trong terminal, và chạy câu lệnh 'pip install -r requirement.txt'

Để cài TA-lib cần theo hướng dẫn ở trang "https://pypi.org/project/TA-Lib/" và cài theo hệ điều hành.

# win: py.exe -3.13 -m pip install ta_lib-0.5.1-cp313-cp313-win_amd64.whl

Sau đó mỗi lần cần chạy simulation chạy câu lệnh 'python BSim-python/BSim.py BSim-python/sample/sample.xml 1'. Nếu muốn ko thấy đầu ra từ simulation thay số 1 bằng số 0

Để lấy report từ output của simulation chạy 'python BlueQuant-alpha-tools/pnl_summary.py BSim-python/sample/pnl/<tên file cần report>'

<!-- run
python ../BSim.py sample.xml -->
