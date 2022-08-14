
python -m pip install -r requirements.txt
IF %1 == ALL (
    pytest -s --alluredir=../allure/results --domain %2 ../UI_Tests
) ELSE (
    pytest -s --alluredir=../allure/results --domain %2 ../UI_Tests/%1
)