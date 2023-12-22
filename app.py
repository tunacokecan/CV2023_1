 #-*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_frozen import Freezer
from PIL import Image
import os

app = Flask(__name__)
freezer = Freezer(app)

#이력서 데이터- 딕셔너리
resume_data = {

    #기본 정보
    'name': 'Heesoo Kim',
    'information': 'I am interested in Project Managing, UX Researching, and Marketing. I am currently studying AI and Python',

    #학력- 리스트형태
    'education': [

        {'position': '전남대학교 자율전공학부(4년)(BS)', 
        'company': 'GPA - 3.71/4.5', 
        'year': '2020.03~ 현재'},
            
        {'position': '서울대학교 자유전공학부 교류학생(BS)', 
        'company': 'GPA - 4.2/4.5', 
        'year': '2022.09~ 2022.12'},

        {'position': '독일 다름슈타트 공대 교환학생 ',
        'company': 'GPA - 3.0/5.0',
        'year': '2023.03 ~ 2023.08'},
    ],


    #경력- 리스트형태
    'experience': [
        {'position': 'Technical University of Darmstadt',
        'company': 'Department of History and Social Sciences (master course)',
        'year': '2023.03 ~ 2023.08',
        'details': [
            'GPA - 3.0 / 5.0',
            'Digital Methods for Heritage Research: An Introduction, Digital Cultural Heritage Information Systems and Processes: readings on the State of the art'
        ]},

    {'position': '한국HCI학회',
        'company': '메타버스 UX 기획 과정 본선 발표 부문 대상',
        'year': '2023.02'},

    {'position': '서울대학교',
        'company': '자유전공학부',
        'year': '2022.06 ~ 2022.08',
        'details': [
            'GPA - 3.74/4.3',
            '미디어인터렉션디자인, VR/AR의 개론및실습, 제품기획론, 주제탐구세미나3, 가상현실입문'
        ]},

    {'position': '한국HCI학회 논문 연구',
        'company': '컴퓨터비전 AI 모델을 활용한 감정반응형 명상공간 메타버스 개발. 한국HCI학회 학술대회.',
        'year': '2022.09 ~ 2022.12'},

    {'position': 'mySUNI Creative Challenge 2022 UX과정',
        'company': '수료',
        'year': '2022.09 ~ 2022.12'},

    {'position': 'Linc 3.0 산학연계 프로그램 [게임제작과정]',
        'company': '수료',
        'year': '2021.02 ~ 2021.05'},

    {'position': '소비의 미학 서포터즈',
        'company': '콘텐츠 에디터 수료',
        'year': '2021.02 ~ 2021.05'},
],

    #출판- 리스트형태
    'publication': [
        {'position': '컴퓨터비전 AI 모델을 활용한 감정반응형 명상공간 메타버스 개발"',
        'company': '김동현, 박고은, 김상엽, 유채원, 김희수, 김희빈, 박지성, 이민구, 윤주현.  HCI Conference Korea (2023): 10-13.',
        'year': '2023'},
         
    ],

    #수상- 리스트형태
    'award': [
        {'position': '2023HCI Conference',
        'company': ' mySUNI Creative Challenge 2022, Grand Prize',
        'year': '2023.03 ~ 2023.08'},
       
    ],

    #보유기술
    'skills': ['Python', 'Adobe Premier Pro' ,'Unity', 'Figma', 'Blender'],

    #프로젝트
# 프로젝트
    'project': [
        {'title': 'Mindly - 컴퓨터비전 AI 모델을 활용한 감정반응형 명상공간 메타버스 ',
        'company': 'SNU Intermedia Lab',
        'year': '2022.09 - 2023.2',
        'details': 'Details about the project.',
        'video_url': 'https://www.youtube.com/watch?v=C8zjVwjON1c' },

        {'title': 'Space Cleaner -  하체 운동 위주의 VR 피트니스 게임 ',
        'company': 'VR/AR의개론및실습',
        'year': '2022.9 - 2022.12',
        'details': 'Details about the project.',
        'video_url': 'https://www.youtube.com/watch?v=5TlNbF5YO0U'},
        ],

      }

def resize_image(input_path, output_path, size):
    original_image = Image.open(input_path)
    resized_image = original_image.resize(size)
    resized_image.save(output_path)

@app.route('/')
def index():
    # 이미지 크기 변환
    original_image_path = 'static/images/profile.jpg'
    resized_image_path = 'static/images/resized.jpg'

    resize_image(original_image_path, resized_image_path, (200, 250))
    return render_template('index.html', resume_data=resume_data)


@app.route('/project/<project_title>')
def project(project_title):
    # 프로젝트 제목을 기반으로 프로젝트 데이터 찾기
    project_data = None
    for project in resume_data['project']:
        if project['title'] == project_title:
            project_data = project
            break

    if project_data:
        return render_template('project.html', project_data=project_data)
    else:
        return 'Project not found', 404
if __name__ == '__main__':
    freezer.freeze()


