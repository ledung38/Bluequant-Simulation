Step 1: Sau khi clone repo về, cd vào thư mục bluequant-simulation , và chạy câu lệnh install library

> `pip install -r requirement.txt`

Step 2: Để cài TA-lib cần theo hướng dẫn ở trang "https://pypi.org/project/TA-Lib/" và cài theo hệ điều hành.

# windown: run

> `py.exe -3.13 -m pip install ta_lib-0.5.1-cp313-cp313-win_amd64.whl`

Step 3: Cd sample forder

> `cd BSim-python/sample`

Step 4:
Run simulation. Nếu muốn ko muốn prinf simulation thay số 1 bằng số 0

> `python ../BSim.py sample.xml 1`

Để lấy report từ output của simulation. tool test:

> `python BlueQuant-alpha-tools/pnl_summary.py BSim-python/sample/pnl/<tên file cần report>`
