from selenium import webdriver
import time
import numpy as np
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#광역시도 선택 함수
def make_data():
    mega_index = 1
    city_index = 1
    store_index = 0
    result_table = []
    #상권버튼 클릭
    while True:
        #상권 버튼 생길 시 까지 대기
        element = wait.until(EC.element_to_be_clickable((By.ID, 'btnDrawMajor')))

        driver.find_element_by_xpath('//*[@id="btnDrawMajor"]').click()

        #로딩 대기
        element = wait.until(EC.element_to_be_clickable((By.ID, 'megaSelList_M')))

        #광역시도 리스트(1~끝까지, 첫번째가 전국)
        mega = driver.find_element_by_class_name('megaSelList')
        mega_li = mega.find_elements_by_tag_name('li')
        mega_li[mega_index].click()

        #로딩 대기
        element = wait.until(EC.element_to_be_clickable((By.ID, 'ctySelList_M')))

        #시군구 리스트(1~끝까지, 첫번째가 전체)
        city = driver.find_element_by_class_name('ctySelList')
        city_li = city.find_elements_by_tag_name('li')
        city_result_text = city_li[city_index].text
        result = [city_result_text]
        city_li[city_index].click()

        #로딩 대기
        element = wait.until(EC.element_to_be_clickable((By.ID, 'major_area')))

        #주요 상권 클릭(1개만)
        driver.find_element_by_xpath('//*[@id="major_area"]/li[1]/a').click()

        #로딩 대기
        element = wait.until(EC.element_to_be_clickable((By.ID, 'majorStoreList')))
                
        #상권 리스트(0~끝까지)
        store_area = driver.find_element_by_class_name('majorStoreSelList')
        store_area_li = store_area.find_elements_by_tag_name('li')
        store_area_li[store_index].click()
        store_index += 1

        if store_index >= len(store_area_li):
            store_index = 0
            city_index += 1

        #확인 버튼 클릭
        driver.find_element_by_xpath('//*[@id="LayerPopCommercialArea"]/div/a[1]').click()

        #업종 선택 (아무거나 상관 없음)
        driver.find_element_by_xpath('//*[@id="upjongSelect"]/div/a').click()
        selector = '#LayerPopCategory > div.layer-pop-footer-grey.ng-scope > a.btn.btn-primary.btm-btn'

        #로딩대기
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        driver.find_element_by_xpath('//*[@id="up1Tab_Q"]/ul/li[1]/ul/li[1]').click()

        #확인
        driver.find_element_by_xpath('//*[@id="LayerPopCategory"]/div[2]/a[1]').click()


        #분석하기 클릭
        selector1 = '#upjongListDiv > ol > li:nth-child(1)'
        element = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector1)))
        driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[2]/div[1]/div[4]/span[2]/a').click()

        #로딩 대기
        selector2 = '#analysisResultinfo > div > table:nth-child(2)'
        element = WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector2)))

        #유동인구 수치 저장

        driver.find_element_by_xpath('//*[@id="resultAnalysisForm"]/div/div[3]/div/div/ul[1]/li[4]/a').send_keys(Keys.ENTER)

        #로딩 대기
        selector3 = '#resultPop > table:nth-child(9)'
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector3)))

        #결과 값
        table = driver.find_element_by_xpath('//*[@id="resultPop"]/table[1]')
        tbody = table.find_element_by_tag_name('tbody')
        head = tbody.find_element_by_tag_name('th')
        rows = tbody.find_element_by_tag_name('tr')
        body= rows.find_elements_by_tag_name("td")

        result.append(head.text)
        for index, value in enumerate(body):
            result_value = value.text
            result.append(result_value)

        #데이터 저장
        result_table.append(result)
        print(city_result_text + ' ' + head.text + ' ' + '저장 완료')
        

        #뒤로가기
        driver.back()

        if city_index >= len(city_li):
            result_table = np.array(result_table)
            pd.DataFrame(result_table).to_csv(r"C:\Users\95yby\Desktop\file.csv", encoding='utf-8-sig')
            print('모든 데이터 저장 완료!!')
            break


driver=webdriver.Chrome(r'C:\Users\95yby\Desktop\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get('http://sg.sbiz.or.kr/index.sg?supDev=1#/analy/mainD/')
driver.find_element_by_xpath('//*[@id="body"]/div/div/div/div/div[3]/div/a').click()
#id, password 입력
elem_login = driver.find_element_by_id('id')
elem_login.clear()
elem_login.send_keys('95ybya')

elem_login = driver.find_element_by_id('pass')
elem_login.clear()
elem_login.send_keys('dbsqud12dms!')

#로그인 버튼 클릭
driver.find_element_by_xpath('/html/body/div/div[2]/form/div/button').click()


#로딩 대기 변수 설정
wait = WebDriverWait(driver, 100)



make_data()