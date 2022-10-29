그래프 화면

<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <!--
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    -->
    <meta name="viewport" content="width=1280">

    <!-- static 폴더 참조 -->
    <!-- 원그래프 js는 각 페이지에서 소환해야됨 (일회성 호출이라서.) -->
    
    <link rel="stylesheet" href="/static/css/style.css?date=0815">
    <!-- favicon -->
    <link rel="icon" href="/static/img/favicon.ico">

    <!-- 웹 참조-->
    <script src="//code.jquery.com/jquery-latest.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
    <script src="https://kit.fontawesome.com/e8a335040d.js" crossorigin="anonymous"></script>

    <!-- 웹 폰트 참조-->
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Courgette&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500&display=swap" rel="stylesheet">

    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-219523848-1"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());
        gtag('config', 'UA-219523848-1');
    </script>

    <title>Please Graduate</title>
</head>

<body>
    <!-- 로고 / 메뉴바-->
    <nav class="navbar">
        <div class="navbar_logo">
            
            <a href="/"><img src="/static/img/logo.png"></a>
        </div>

        <ul class="navbar_menu">

            <!-- <div class="navbar_logo">
                
                <a href="/"><img src="/static/img/logo.png"></a>
            </div> -->

            <li>
                <a href='https://forms.gle/f2vUqVg9wQFneBLf7' target="_blank">피드백하기</a>
            </li>

            <li>
                <a href='/statistics/'>꿀교양찾기</a>
            </li>

            
            <li>
                <a href='/mypage/'>마이페이지</a>
            </li>
            

            <li>
                <!-- 로그인 세션 활용 -->
                
                <a href='javascript:logout()'>로그아웃</a>
                
            </li>
        </ul>
    </nav>


    
<div class="lcontainer">

    <!-- 총학점 -->
    <div class="fcontainer">
        <div class="resultbox container0">
            <div class="name name0">
                Total
            </div>
            <div class="box">
                <div class="chart_box" id="chart0">
                    <strong class="total_strong"></strong>
                </div>
                <div class="Sbox">
                    <div class="gbox total_gbox">
                        <span class="grade Grade">학번</span>
                        <span class="t" id="studentnumber"></span>
                    </div>
                    <div class="gbox total_gbox">
                        <span class="grade Grade">이름</span>
                        <span class="t" id="name"></span>
                    </div>
                    <div class="gbox total_gbox">
                        <span class="grade Grade">총 기준 학점
                        </span>
                        <span class="t" id="totalgrade"></span>
                    </div>
                    <div>
                        <div class="gbox total_gbox">
                            <span class="grade Grade">총 이수 학점
                            </span>

                            <span class="t" id="mytotalgrade"></span>
                        </div>
                    </div>
                    <div>
                        <div class="gbox Gbox total_gbox">
                            <span class="cap"><i class="fas fa-graduation-cap"></i></span>

                            <div class="T" id="cangraduate"> </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="rcontainer">
        <!-- 복필/연선 -->
        
        <div class="resultbox">
            <div class="name">
                
                복수전공 필수
                
            </div>
            <div class="box">
                <div id="chart_multi_me">
                    <strong></strong>
                </div>
                <div class="sbox">
                    <div class="gbox" style="margin-top:-1rem">
                        <span class="grade">기준 학점</span>
                        <span class="r" id="grade_multi_me"></span>
                    </div>
                    <div class="gbox" style="margin-top:-3rem">
                        <span class="grade">이수 학점</span>
                        <span class="r" id="my_grade_multi_me"></span>
                    </div>
                </div>
            </div>
        </div>

        <div class="resultbox">
            <div class="name">
                
                복수전공 선택
                
            </div>
            <div class="box">
                <div id="chart_multi_ms">
                    <strong></strong>
                </div>
                <div class="sbox">
                    <div class="gbox" style="margin-top:-1rem">
                        <span class="grade">기준 학점</span>
                        <span class="r" id="grade_multi_ms"></span>
                    </div>
                    <div class="gbox" style="margin-top:-3rem">
                        <span class="grade" style="letter-spacing: -0.2px;">이수 학점</span>
                        <span class="r" id="my_grade_multi_ms"></span>
                        <span class="tooltip" id="multi_remain" style="color:#d32f2f; margin-left:-0.5rem"></span>
                        <div class="tooltip_text">
                            
                            복필 영역에서 기준 학점 초과시 복선 학점으로 인정됩니다.
                            
                        </div>
                    </div>

                    
                </div>
            </div>
        </div>
        

        <!-- 전필 -->
        <div class="resultbox">
            <!-- 타이틀 -->
            <div class="name">
                전공 필수
                <span class="tooltip">
                    <span class='tip_div'>Tip</span>
                </span>
                <!-- 클릭시 툴팁 -->
                <div class="tooltip_text">
                    <p>&#183; 전공필수 과목에서 기준보다 <span class='tooltip_span'>초과되는 학점</span>은 전공선택 학점에 추가됩니다.</p>
                    <p>&#183; 학과에 따라 필수로 들어야하는 전필과목이 있을 수 있습니다. (학과 홈페이지 참조)</p>
                    <p>&#183; 한 가지 조건을 만족했을 경우 통과합니다.</p>
                    <p class='tooltip_sub_p'>1. 전공필수 과목으로 기준학점을 만족해야합니다.</p>
                </div>
            </div>
            <!-- 내용 -->
            <div class="box">
                <!-- 원 그래프 -->
                <div id="chart1">
                    <strong></strong>
                </div>
                <!-- 텍스트 영역 -->
                <div class="sbox">
                    <div class="gbox">
                        <span class="grade">기준 학점</span>
                        <span class="r" id="grade1"></span>
                    </div>
                    <div class="gbox">
                        <span class="grade">이수 학점</span>
                        <span class="r" id="mygrade1"></span>
                    </div>
                    <button class="rbutton" id="myBtn1">Recommend</button>
                </div>
            </div>
        </div>

        <!-- 전선 -->
        <div class="resultbox">
            <div class="name">
                전공 선택
                <span class="tooltip">
                    <span class='tip_div'>Tip</span>
                </span>
                <div class="tooltip_text">
                    <p>&#183; 학점 계산시 <span class='tooltip_span'>초과된 전필 학점</span>이 있다면 전선 학점에 더해진 뒤 계산됩니다.</p>
                    <p>&#183; 한 가지 조건을 만족했을 경우 통과합니다.</p>
                    <p class='tooltip_sub_p'>1. 전공선택 과목으로 기준학점을 만족해야합니다.</p>
                </div>
            </div>
            <div class="box">
                <div id="chart2">
                    <strong></strong>
                </div>
                <div class="sbox">
                    <div class="gbox">
                        <span class="grade">기준 학점</span>
                        <span class="r" id="grade2"></span>
                    </div>
                    <div class="gbox">
                        <span class="grade" >이수 학점</span>
                        <span class="r" id="mygrade2"></span>
                        <span class="tooltip tooltip_info" id="myremain" style="margin-left:-0.5rem;"></span>
                        <div class="tooltip_text">
                            전필 영역에서 기준 학점 초과시 전선 학점으로 인정됩니다.
                        </div>
                    </div>
                    <button class="rbutton" id="myBtn2">Recommend</button>
                </div>
            </div>
        </div>

        <!-- 교필/중필 -->
        
        <div class="resultbox">
            <div class="name">
                공통교양필수
                <span class="tooltip">
                    <span class='tip_div'>Tip</span>
                </span>
                <div class="tooltip_text">
                    <p>&#183; 22년도부터 <span class='tooltip_span'>교양필수(교필) -> 공통교양필수(공필)</span>로 이수구분명이 변경되었습니다.</p>
                    <p>&#183; 한 가지 조건을 만족했을 경우 통과합니다.</p>
                    <p class='tooltip_sub_p'>1. 해당 영역에서 정해진 필수과목을 모두 이수해야합니다.</p>
                    <p class='tooltip_sub_p'>&nbsp;&nbsp;&nbsp;- <span class='tooltip_span'>기준 학점과 상관없이</span> 필수과목만 모두 이수하면 됩니다.</p>
                    <p class='tooltip_sub_p'>&nbsp;&nbsp;&nbsp;- 필수과목의 이수구분이 <span class='tooltip_span'>변경되어도</span> 필수과목을 이수한 것으로 인정됩니다.</p>
                    <p class='tooltip_sub_p'>&nbsp;&nbsp;&nbsp;- 해당 과목이 폐강된 경우 동일과목으로 대체 이수해야합니다.</p>
                </div>
            </div>
            <div class="box">
                <div id="chart3">
                    <strong></strong>
                </div>
                <div class="sbox">
                    <div class="gbox">
                        <span class="grade">필수 과목</span>
                        <span class="r" id="grade3"></span>
                    </div>
                    <div class="gbox">
                        <span class="grade">이수 과목</span>
                        <span class="r" id="mygrade3"></span>
                    </div>
                    <button class="rbutton" id="myBtn3">Recommend</button>
                </div>
            </div>
        </div>
        

        <!-- 교선/중선 -->
        
        <div class="resultbox">
            <div class="name">
                교양 선택
                <span class="tooltip">
                    <span class='tip_div'>Tip</span>
                </span>
                <div class="tooltip_text">
                    <p>&#183; 22년도부터 교선1, 교선2가 통합되었습니다.</p>
                    <p class='tooltip_sub_p'>- 단, 통합 이전에 수강한 교선2는 교선영역 기준학점에 <span class='tooltip_span'>포함되지 않습니다.</span></p>
                    <p class='tooltip_sub_p'>- 선택영역도 5개 영역 -> 6개 영역으로 통합되었습니다.</p>
                    <p>&#183; 세 가지 조건을 만족했을 경우 통과합니다.</p>
                    <p class='tooltip_sub_p'>1. 교양선택 과목으로 기준학점을 만족해야합니다.</p>
                    <p class='tooltip_sub_p'>2. 교양선택 영역에서 정해진 필수과목을 모두 이수해야합니다.</p>
                    <p class='tooltip_sub_p'>&nbsp;&nbsp;&nbsp;- <span class='tooltip_span'>기준 학점과 상관없이</span> 필수과목만 모두 이수하면 됩니다.</p>
                    <p class='tooltip_sub_p'>&nbsp;&nbsp;&nbsp;- 필수과목의 이수구분이 <span class='tooltip_span'>변경되어도</span> 필수과목을 이수한 것으로 인정됩니다.</p>
                    <p class='tooltip_sub_p'>&nbsp;&nbsp;&nbsp;- 해당 과목이 폐강된 경우 동일과목으로 대체 이수해야합니다.</p>
                    <p class='tooltip_sub_p'>3. 과목마다 '선택영역'이 존재하고, 6가지의 선택영역 중 3가지 이상 이수해야합니다.</p>
                </div>
            </div>
            <div class="box">
                <div id="chart4">
                    <strong></strong>
                </div>
                <div class="sbox">
                    <div class="gbox">
                        <span class="grade">기준 학점</span>
                        <span class="r" id="grade4"></span>
                    </div>
                    <div class="gbox">
                        <span class="grade">이수 학점</span>
                        <span class="r" id="mygrade4"></span>
                    </div>
                    <div class="gbox">
                        <span class="grade">필수 과목</span>
                        <span class="r" id="cs_p"></span>
                    </div>
                    <div class="gbox">
                        <span class="grade">이수 영역</span>
                        <span class="r" id="myarea4"></span>
                    </div>
                    <button class="rbutton" id="myBtn4">Recommend</button>
                </div>
            </div>
        </div>
        

        <!-- 균필 -->
        

        <!-- 기교 -->
        
        <div class="resultbox">
            <div class="name">
                학문기초교양필수
                <span class="tooltip">
                    <span class='tip_div'>Tip</span>
                </span>
                <div class="tooltip_text">
                    <p>&#183; 22년도부터 <span class='tooltip_span'>학문기초교양(기교) -> 학문기초교양필수(기필)</span>로 이수구분명이 변경되었습니다.</p>
                    <p>&#183; 한 가지 조건을 만족했을 경우 통과합니다.</p>
                    <p class='tooltip_sub_p'>1. 해당 영역에서 정해진 필수과목을 모두 이수해야합니다.</p>
                    <p class='tooltip_sub_p'>&nbsp;&nbsp;&nbsp;- <span class='tooltip_span'>기준 학점과 상관없이</span> 필수과목만 모두 이수하면 됩니다.</p>
                    <p class='tooltip_sub_p'>&nbsp;&nbsp;&nbsp;- 필수과목의 이수구분이 <span class='tooltip_span'>변경되어도</span> 필수과목을 이수한 것으로 인정됩니다.</p>
                    <p class='tooltip_sub_p'>&nbsp;&nbsp;&nbsp;- 해당 과목이 폐강된 경우 동일과목으로 대체 이수해야합니다.</p>
                    <p><span class='tooltip_span'>※ 화학과는 선택과목 조건이 추가로 존재합니다.</span></p>
                </div>
            </div>
            <div class="box">
                <div id="chart5">
                    <strong></strong>
                </div>
                <div class="sbox">
                    <div class="gbox">
                        <span class="grade">필수 과목</span>
                        <span class="r" id="grade5"></span>
                    </div>
                    <div class="gbox">
                        <span class="grade">이수 과목</span>
                        <span class="r" id="mygrade5"></span>
                    </div>
                    
                    <button class="rbutton" id="myBtn5">Recommend</button>
                </div>
            </div>
        </div>
        

        <!-- 영어 -->
        
        <div class="resultbox">
            <div class="name name8">
                영어졸업인증
                <span class="tooltip">
                    <span class='tip_div'>Tip</span>
                </span>
                <div class="tooltip_text" style='left: -230px;'>
                    <p>&#183; 총 3가지 통과 방법이 존재하고, 이 중 하나만 만족하면 통과합니다.</p>
                    <p class='tooltip_sub_p'>1. 5가지 공인영어인증시험 중, 하나의 시험에서 기준 점수를 만족</p>
                    <p class='tooltip_sub_p'>2. Intensive English 과목을 이수</p>
                    <p class='tooltip_sub_p'>3. 초과학기(or 졸업유예) 1년 이상 면제</p>
                    <p>&#183; 영어인증시험 성적은 정해진 기간에 <span class='tooltip_span'>교양영어실</span>에 방문 제출해야합니다.</p>
                    <p>&#183; 모든 졸업 기준 만족 후 영어 성적을 제출하지 않으면 <span class='tooltip_span'>졸업유예</span> 상태가 됩니다.</p>
                </div>
            </div>
            <div class="box ">
                <div id="chart8">
                    <strong></strong>
                </div>
                <div class="sbox">
                    <div class="gbox">
                        <span class="grade" style="font-weight: bold;">OPIc</span>
                    </div>
                    <div class="gbox">
                        <span class="grade">통과 여부</span>
                        <span class="r" id="grade8"></span>
                    </div>
                    <button class="rbutton" id="myBtn8">Recommend</button>
                </div>
            </div>
        </div>
        

        <!-- 고전독서 -->
        <div class="resultbox">
            <div class="name">
                고전독서인증
                <span class="tooltip">
                    <span class='tip_div'>Tip</span>
                </span>
                <div class="tooltip_text">
                    <p>&#183; 각 4개 영역에서의 기준 권수를 만족하면 통과합니다. (총 10권)</p>
                    <p>&#183; 7학기를 기점으로 인증 방법이 나뉘며, 다양한 방법으로 권수를 채울 수 있습니다.</p>

                    <p>&#183; 7학기 시작 전 (3-2까지 가능)</p>
                    <p class='tooltip_sub_p'>1. <a class="link_site" target="_blank"
                        href="http://classic.sejong.ac.kr/">고전독서인증센터</a> 에서 시험 예약 후 응시하기</p>
                    <p class='tooltip_sub_p'>2. 고전강독 강의 수강 대체인증</p>
                    <p class='tooltip_sub_p'>3. 학술정보원주최 독서경시대회 입상</p>
                    <p class='tooltip_sub_p'>4. 대양휴머니티칼리지주최 고전PT대회 1차 예선 통과</p>

                    <p>&#183; 7학기 시작 후 (4학년 이후)</p>
                    <p class='tooltip_sub_p'>4학년이 되었는데 기준을 통과하지 못했다면... 😱 <br>
                        위 4가지 방법으로 5권까지 이수 후, <span class='tooltip_span'>고전특강</span> 강의 수강시 통과
                    </p>
                    <p class='tooltip_sub_p'><span class='tooltip_span'>※ 5권 이상 이수하지 못했다면 강의 수강 불가</span></p>

                </div>
            </div>

            <div class="box">
                <div id="chart7">
                    <strong></strong>
                </div>
                
                <div class="sbox Y">
                    <div class="gbox">
                        <span class="grade p">이수 기준</span>
                    </div>
                    <div class="gbox">
                        <span class="grade y">서양</span>
                        <span class="book" id="swbook"></span>/ 4권
                    </div>
                    <div class="gbox">
                        <span class="grade y">동양</span>
                        <span class="book" id="wbook"></span>/ 2권
                    </div>
                    <div class="gbox">
                        <span class="grade y">동서양</span>
                        <span class="book" id="sbook"></span>/ 3권
                    </div>
                    <div class="gbox">
                        <span class="grade y">과학</span>
                        <span class="book" id="scbook"></span>/ 1권
                    </div>
                </div>
                
            </div>
        </div>
    </div>
</div>


<!-- 추천 모달-->

<!-- 전필 -->
<div id="myModal1" class="modal">
    <div class="modal-content">
        <span class="close" id="close1">&times;</span>
        <br>
        <div style="padding: 1rem; text-align: center;">
            <!-- 추천과목 -->
            <div style="font-size : 1.5rem;"><i class="my_i fas fa-check-circle"></i> 추천과목
            </div>
            <div class="mydiv">같은 학과 사용자들이 가장 많이 수강했던 전필과목 순으로 추천합니다.</div>
            <hr>
            
            <div class="partdiv">
                
                <span style="color:#17a55e"> 기준 학점을 만족했습니다. </span>
                
            </div>
        </div>
    </div>
</div>

<!-- 전선 -->
<div id="myModal2" class="modal">
    <div class="modal-content">
        <span class="close" id="close2">&times;</span>
        <br>
        <div class="modal_div">
            <div class="p_div">
                <!-- 추천과목 -->
                <div style="font-size : 1.5rem;"><i class="my_i fas fa-check-circle"></i> 추천과목
                </div>
                <div class="mydiv">같은 학과 사용자들이 가장 많이 수강했던 전선과목 순으로 추천합니다.</div>
                <hr>
                
                
                <table class="mytable">
                    <tr class="myth" style="background-color: #f8f8f8;">
                        <th style="border-right :1px solid #cccccc; width:12%">학수번호</th>
                        <th style="border-right :1px solid #cccccc; width:40%">과목명</th>
                        <th style="border-right :1px solid #cccccc; width:16%">이수구분</th>
                        <th style="border-right :1px solid #cccccc; width:12%">선택영역</th>
                        <th style="border-right :1px solid #cccccc; width:8%">학점</th>
                        <th style="width:12%">수강순위</th>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">5611</td>
                        <td class="mytd">디지털논리회로</td>
                        <td class="mytd">전선</td>
                        <td class="mytd"></td>
                        <td class="mytd">3</td>
                        <td class="mytd" style="border-right :0px">1</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">4596</td>
                        <td class="mytd">반도체공학</td>
                        <td class="mytd">전선</td>
                        <td class="mytd"></td>
                        <td class="mytd">3</td>
                        <td class="mytd" style="border-right :0px">2</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">9662</td>
                        <td class="mytd">전자회로설계</td>
                        <td class="mytd">전선</td>
                        <td class="mytd"></td>
                        <td class="mytd">3</td>
                        <td class="mytd" style="border-right :0px">3</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">7721</td>
                        <td class="mytd">반도체소자설계</td>
                        <td class="mytd">전선</td>
                        <td class="mytd"></td>
                        <td class="mytd">3</td>
                        <td class="mytd" style="border-right :0px">4</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">5130</td>
                        <td class="mytd">JAVA프로그래밍</td>
                        <td class="mytd">전선</td>
                        <td class="mytd"></td>
                        <td class="mytd">3</td>
                        <td class="mytd" style="border-right :0px">5</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">7720</td>
                        <td class="mytd">디스플레이공학</td>
                        <td class="mytd">전선</td>
                        <td class="mytd"></td>
                        <td class="mytd">3</td>
                        <td class="mytd" style="border-right :0px">6</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">4475</td>
                        <td class="mytd">자동제어</td>
                        <td class="mytd">전선</td>
                        <td class="mytd"></td>
                        <td class="mytd">3</td>
                        <td class="mytd" style="border-right :0px">7</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">9659</td>
                        <td class="mytd">전자기2</td>
                        <td class="mytd">전선</td>
                        <td class="mytd"></td>
                        <td class="mytd">3</td>
                        <td class="mytd" style="border-right :0px">8</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">7722</td>
                        <td class="mytd">전자회로2</td>
                        <td class="mytd">전선</td>
                        <td class="mytd"></td>
                        <td class="mytd">3</td>
                        <td class="mytd" style="border-right :0px">9</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">4268</td>
                        <td class="mytd">데이터구조론</td>
                        <td class="mytd">전선</td>
                        <td class="mytd"></td>
                        <td class="mytd">3</td>
                        <td class="mytd" style="border-right :0px">10</td>
                    </tr>
                    
                </table>
                
                
                <div class="partdiv">
                    
                    <span style="color:#d32f2f">9 학점이 부족합니다</span>
                    
                </div>
            </div>
        </div>
    </div>
</div>

<!-- 중필/교필 -->
<div id="myModal3" class="modal">
    <div class="modal-content">
        <span class="close" id="close3">&times;</span>
        <br>
        <div class="modal_div">
            <!-- 필수과목 -->
            <div class="p_div">
                <div style="font-size : 1.5rem;"><i class="fas fa-check-circle"></i> 필수과목 목록
                </div>
                <div class="mydiv">필수과목을 모두 이수해야 졸업요건을 충족합니다.</div>
                <hr>
                <table class="mytable">
                    <tr class="myth" style="background-color: #f8f8f8;">
                        <th style="border-right :1px solid #cccccc; width:15%">학수번호</th>
                        <th style="border-right :1px solid #cccccc; width:40%">과목명</th>
                        <th style="border-right :1px solid #cccccc; width:15%">이수구분</th>
                        <th style="border-right :1px solid #cccccc; width:15%">선택영역</th>
                        <th style="width:15%">학점</th>
                    </tr>
                    
                    
                    <tr class="mytr">
                        
                        <td class="mytd">10351</td>
                        <td class="mytd">대학생활과진로설계</td>
                        <td class="mytd">교필</td>
                        <td class="mytd">역량강화</td>
                        <td class="mytd" style="border-right :0px">1</td>
                    </tr>
                    
                    
                    <tr class="mytr">
                        
                        <td class="mytd">10352</td>
                        <td class="mytd">English Listening Practice 1</td>
                        <td class="mytd">교필</td>
                        <td class="mytd">학문기초</td>
                        <td class="mytd" style="border-right :0px">2</td>
                    </tr>
                    
                    
                    <tr class="mytr">
                        
                        <td class="mytd">10354</td>
                        <td class="mytd">English Reading Practice 1</td>
                        <td class="mytd">교필</td>
                        <td class="mytd">학문기초</td>
                        <td class="mytd" style="border-right :0px">2</td>
                    </tr>
                    
                    
                    <tr class="mytr" style="color: #d32f2f">
                        
                        <td class="mytd">8364</td>
                        <td class="mytd">세종사회봉사1</td>
                        <td class="mytd">교선</td>
                        <td class="mytd">자기계발과진로</td>
                        <td class="mytd" style="border-right :0px">1</td>
                    </tr>
                    
                    
                    <tr class="mytr">
                        
                        <td class="mytd">9030</td>
                        <td class="mytd">취업역량개발론</td>
                        <td class="mytd">교필</td>
                        <td class="mytd">역량강화</td>
                        <td class="mytd" style="border-right :0px">1</td>
                    </tr>
                    
                    
                    <tr class="mytr">
                        
                        <td class="mytd">9067</td>
                        <td class="mytd">문제해결을위한글쓰기와발표</td>
                        <td class="mytd">공필</td>
                        <td class="mytd"></td>
                        <td class="mytd" style="border-right :0px">3</td>
                    </tr>
                    
                    
                    <tr class="mytr">
                        
                        <td class="mytd">9068</td>
                        <td class="mytd">서양철학:쟁점과토론</td>
                        <td class="mytd">공필</td>
                        <td class="mytd"></td>
                        <td class="mytd" style="border-right :0px">3</td>
                    </tr>
                    
                </table>
                <div class="partdiv">
                    
                    <span style="color:#d32f2f">필수과목이 부족합니다</span>
                    
                </div>

                
                <!-- 필수과목 추천 -->
                <div style="font-size : 1.5rem;"><i class="my_i fas fa-check-circle"></i> 필수과목 추천
                </div>
                <div class="mydiv">
                    최근 1년의 강의목록 중 동일 과목으로 추천합니다.<br>
                    (다른 과목이 추천될 때 : 과목명이 변경된 것입니다. / 과목이 추천되지 않을 때 : 더 이상 열리지 않는 과목입니다.)
                </div>
                <hr>
                <table class="mytable">
                    <tr class="myth" style="background-color: #f8f8f8;">
                        <th style="border-right :1px solid #cccccc; width:15%">학수번호</th>
                        <th style="border-right :1px solid #cccccc; width:40%">과목명</th>
                        <th style="border-right :1px solid #cccccc; width:15%">이수구분</th>
                        <th style="border-right :1px solid #cccccc; width:15%">선택영역</th>
                        <th style="width:15%">학점</th>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">8364</td>
                        <td class="mytd">세종사회봉사1</td>
                        <td class="mytd">교선</td>
                        <td class="mytd">자기계발과진로</td>
                        <td class="mytd" style="border-right :0px">1</td>
                    </tr>
                    
                </table>
                
            </div>
        </div>
    </div>
</div>

<!-- 중선/교선 -->
<div id="myModal4" class="modal">
    <div class="modal-content">
        <span class="close" id="close4">&times;</span>
        <br>
        <div class="modal_div">
            <div class="p_div">
                <div style="font-size : 1.5rem;"><i class="fas fa-check-circle"></i> 선택영역 현황
                </div>
                <div class="mydiv">'선택영역'을 필수로 3개 이상 이수해야 졸업요건을 충족합니다.</div>
                <hr>
                <table class="mytable" style="padding-bottom:1rem">
                    <tr class="myth" style="background-color: #f8f8f8;">
                        <th style="border-right :1px solid #cccccc; width:16%">사상과역사
                        </th>
                        <th style="border-right :1px solid #cccccc; width:16%">사회와문화
                        </th>
                        <th style="border-right :1px solid #cccccc; width:16%">자연과과학기술
                        </th>
                        <th style="border-right :1px solid #cccccc; width:16%">세계와지구촌
                        </th>
                        <th style="border-right :1px solid #cccccc; width:16%">예술과체육
                        </th>
                        <th style="width:16%">
                            자기계발과진로<br>
                            <span style="font-size: 1rem;">(융합과창업)</span>
                        </th>
                    </tr>
                    <tr class="mytr">
                        
                        
                        <td class="mytd" style='color:#17a55e; font-weight: bold;'>
                        
                            이수
                        </td>
                        
                        
                        <td class="mytd">
                        
                            미이수
                        </td>
                        
                        
                        <td class="mytd" style='color:#17a55e; font-weight: bold;'>
                        
                            이수
                        </td>
                        
                        
                        <td class="mytd">
                        
                            미이수
                        </td>
                        
                        
                        <td class="mytd">
                        
                            미이수
                        </td>
                        
                        
                        <td class="mytd" style='color:#17a55e; font-weight: bold;'>
                        
                            이수
                        </td>
                        
                    </tr>
                </table>
                <div class="partdiv">
                    
                    <span style="color:#17a55e">선택영역 조건을 만족하셨습니다</span>
                    
                </div>
            </div>
            <!-- 필수과목 -->
            <div class="p_div">
                <div style="font-size : 1.5rem;"><i class="fas fa-check-circle"></i> 필수과목 목록
                </div>
                <div class="mydiv">필수과목을 모두 이수해야 졸업요건을 충족합니다.</div>
                <hr>
                <table class="mytable">
                    <tr class="myth" style="background-color: #f8f8f8;">
                        <th style="border-right :1px solid #cccccc; width:15%">학수번호</th>
                        <th style="border-right :1px solid #cccccc; width:40%">과목명</th>
                        <th style="border-right :1px solid #cccccc; width:15%">이수구분</th>
                        <th style="border-right :1px solid #cccccc; width:15%">선택영역</th>
                        <th style="width:15%">학점</th>
                    </tr>
                    
                    
                    <tr class="mytr">
                        
                        <td class="mytd">9489</td>
                        <td class="mytd">세계사:인간과문명</td>
                        <td class="mytd">교선</td>
                        <td class="mytd">사상과역사</td>
                        <td class="mytd" style="border-right :0px">3</td>
                    </tr>
                    
                    
                    <tr class="mytr">
                        
                        <td class="mytd">9791</td>
                        <td class="mytd">고급프로그래밍입문-C</td>
                        <td class="mytd">교선1</td>
                        <td class="mytd">자연과과학기술</td>
                        <td class="mytd" style="border-right :0px">3</td>
                    </tr>
                    
                </table>
                <div class="partdiv">
                    
                    <span style="color:#17a55e">필수과목 조건을 만족하셨습니다</span>
                    
                </div>
            </div>
            <!-- 필수과목 추천 -->
            

            <!-- 추천과목 -->
            
            <div class="p_div">
                <div style="font-size : 1.5rem;"><i class="my_i fas fa-check-circle"></i> 추천과목
                </div>
                <div class="mydiv">
                    전체 사용자들이 가장 많이 수강했던 교양과목 순으로 추천합니다. (부족한 필수영역을 우선으로 보여줍니다)
                </div>
                <hr>
                <table class="mytable">
                    <tr class="myth" style="background-color: #f8f8f8;">
                        <th style="border-right :1px solid #cccccc; width:12%">학수번호</th>
                        <th style="border-right :1px solid #cccccc; width:40%">과목명</th>
                        <th style="border-right :1px solid #cccccc; width:16%">이수구분</th>
                        <th style="border-right :1px solid #cccccc; width:12%">선택영역</th>
                        <th style="border-right :1px solid #cccccc; width:8%">학점</th>
                        <th style="width:12%">수강순위</th>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">9938</td>
                        <td class="mytd">동서양고전문학강독</td>
                        <td class="mytd">교선</td>
                        <td class="mytd">사상과역사</td>
                        <td class="mytd">1</td>
                        <td class="mytd" style="border-right :0px">1</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">9031</td>
                        <td class="mytd">한국현대사의이해</td>
                        <td class="mytd">교선</td>
                        <td class="mytd">사상과역사</td>
                        <td class="mytd">3</td>
                        <td class="mytd" style="border-right :0px">2</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">4763</td>
                        <td class="mytd">과학사</td>
                        <td class="mytd">교선</td>
                        <td class="mytd">자연과과학기술</td>
                        <td class="mytd">3</td>
                        <td class="mytd" style="border-right :0px">3</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">6279</td>
                        <td class="mytd">정보사회의사이버윤리</td>
                        <td class="mytd">교선</td>
                        <td class="mytd">사상과역사</td>
                        <td class="mytd">3</td>
                        <td class="mytd" style="border-right :0px">4</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">8913</td>
                        <td class="mytd">동양고전강독1</td>
                        <td class="mytd">교선</td>
                        <td class="mytd">사상과역사</td>
                        <td class="mytd">1</td>
                        <td class="mytd" style="border-right :0px">5</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">9057</td>
                        <td class="mytd">서양고전강독3</td>
                        <td class="mytd">교선</td>
                        <td class="mytd">사상과역사</td>
                        <td class="mytd">1</td>
                        <td class="mytd" style="border-right :0px">6</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">8933</td>
                        <td class="mytd">서양고전강독2</td>
                        <td class="mytd">교선</td>
                        <td class="mytd">사상과역사</td>
                        <td class="mytd">1</td>
                        <td class="mytd" style="border-right :0px">7</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">8914</td>
                        <td class="mytd">서양고전강독1</td>
                        <td class="mytd">교선</td>
                        <td class="mytd">사상과역사</td>
                        <td class="mytd">1</td>
                        <td class="mytd" style="border-right :0px">8</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">7221</td>
                        <td class="mytd">진로설정과자기계발</td>
                        <td class="mytd">교선</td>
                        <td class="mytd">자기계발과진로</td>
                        <td class="mytd">2</td>
                        <td class="mytd" style="border-right :0px">9</td>
                    </tr>
                    
                    <tr class="mytr">
                        <td class="mytd">7082</td>
                        <td class="mytd">취업과진로</td>
                        <td class="mytd">교선</td>
                        <td class="mytd">자기계발과진로</td>
                        <td class="mytd">2</td>
                        <td class="mytd" style="border-right :0px">10</td>
                    </tr>
                    
                </table>
                <div class="partdiv">
                    <a href="/statistics/" style="color:rgb(164, 26, 55); text-decoration : underline">더 추천받고 싶다면 클릭! 🚗</a>
                </div>
            </div>
            
        </div>
    </div>
</div>

<!-- 균필 -->
<div id="myModal9" class="modal">
    <div class="modal-content">
        <span class="close" id="close9">&times;</span>
        <br>
        <div class="modal_div">
            <div class="p_div">
                <div style="font-size : 1.5rem;"><i class="fas fa-check-circle"></i> 선택영역 현황
                </div>
                <div class="mydiv">'선택영역'을 필수로 2개 이상 이수해야 졸업요건을 충족합니다.</div>
                <hr>
                <table class="mytable" style="padding-bottom:1rem; width:65%">
                    <tr class="myth" style="background-color: #f8f8f8;">
                        <th style="border-right :1px solid #cccccc;"></th>
                        <th style="border-right :1px solid #cccccc;"></th>
                        <th></th>
                    </tr>
                    <tr class="mytr">
                        
                    </tr>
                </table>
                <div class="partdiv">
                    
                    <span style="color:#d32f2f">선택영역이 부족합니다</span>
                    
                </div>
            </div>
            <!-- 과목 추천 -->
            
            <div class="p_div">
                <div style="font-size : 1.5rem;"><i class="my_i fas fa-check-circle"></i> 추천과목
                </div>
                <div class="mydiv">
                    듣지 않은 과목 중, 부족한 선택영역의 과목을 추천합니다.
                </div>
                <hr>
                <table class="mytable">
                    <tr class="myth" style="background-color: #f8f8f8;">
                        <th style="border-right :1px solid #cccccc; width:15%">학수번호</th>
                        <th style="border-right :1px solid #cccccc; width:40%">과목명</th>
                        <th style="border-right :1px solid #cccccc; width:15%">이수구분</th>
                        <th style="border-right :1px solid #cccccc; width:15%">선택영역</th>
                        <th style="width:15%">학점</th>
                    </tr>
                    
                </table>
                <br><br><br>
            </div>
            
        </div>
    </div>
</div>


<!-- 기교 -->
<div id="myModal5" class="modal">
    <div class="modal-content">
        <span class="close" id="close5">&times;</span>
        <br>
        <div class="modal_div">
            <!-- 필수과목 -->
            <div class="p_div">
                <div style="font-size : 1.5rem;"><i class="fas fa-check-circle"></i> 필수과목 목록
                </div>
                <div class="mydiv">필수과목을 모두 이수해야 졸업요건을 충족합니다.</div>
                <hr>
                <table class="mytable">
                    <tr class="myth" style="background-color: #f8f8f8;">
                        <th style="border-right :1px solid #cccccc; width:15%">학수번호</th>
                        <th style="border-right :1px solid #cccccc; width:40%">과목명</th>
                        <th style="border-right :1px solid #cccccc; width:15%">이수구분</th>
                        <th style="border-right :1px solid #cccccc; width:15%">선택영역</th>
                        <th style="width:15%">학점</th>
                    </tr>
                    
                    
                    <tr class="mytr">
                        
                        <td class="mytd">10140</td>
                        <td class="mytd">일변수미적분학</td>
                        <td class="mytd">기교</td>
                        <td class="mytd">생명과 과학</td>
                        <td class="mytd" style="border-right :0px">3</td>
                    </tr>
                    
                    
                    <tr class="mytr">
                        
                        <td class="mytd">2647</td>
                        <td class="mytd">일반물리학및실험1</td>
                        <td class="mytd">기교</td>
                        <td class="mytd">생명과 과학</td>
                        <td class="mytd" style="border-right :0px">3</td>
                    </tr>
                    
                    
                    <tr class="mytr">
                        
                        <td class="mytd">2649</td>
                        <td class="mytd">일반물리학및실험2</td>
                        <td class="mytd">기교</td>
                        <td class="mytd">생명과 과학</td>
                        <td class="mytd" style="border-right :0px">3</td>
                    </tr>
                    
                    
                    <tr class="mytr">
                        
                        <td class="mytd">2703</td>
                        <td class="mytd">일반화학</td>
                        <td class="mytd">기교</td>
                        <td class="mytd">생명과 과학</td>
                        <td class="mytd" style="border-right :0px">3</td>
                    </tr>
                    
                    
                    <tr class="mytr">
                        
                        <td class="mytd">304</td>
                        <td class="mytd">공업수학1</td>
                        <td class="mytd">기필</td>
                        <td class="mytd"></td>
                        <td class="mytd" style="border-right :0px">3</td>
                    </tr>
                    
                    
                    <tr class="mytr">
                        
                        <td class="mytd">307</td>
                        <td class="mytd">공업수학2</td>
                        <td class="mytd">기필</td>
                        <td class="mytd"></td>
                        <td class="mytd" style="border-right :0px">3</td>
                    </tr>
                    
                </table>
                <div class="partdiv">
                    
                    <span style="color:#17a55e">필수과목 조건을 만족하셨습니다</span>
                    
                </div>

                

                <!-- 화학과 기교에서는 추가 조건 붙음 !!! -->
                

            </div>
        </div>
    </div>
</div>

<!-- 영어인증 -->
<div id="myModal8" class="modal">
    <div class="modal-content">
        <span class="close" id="close8">&times;</span>
        <br>
        <div class="modal_div">
            <div class="p_div">

                <div style="font-size : 1.5rem;"><i class="fas fa-check-circle"></i>영어 통과 기준
                </div>
                <div class="mydiv">통과 기준 중 하나만 만족하면 통과입니다.</div>
                <hr>
                <table class="mytable">
                    <tr class="myth" style="background-color: #f8f8f8;">
                        <th style="border-right :1px solid #cccccc; width:14.2%">TOEIC</th>
                        <th style="border-right :1px solid #cccccc; width:14.2%">TOEFL</th>
                        <th style="border-right :1px solid #cccccc; width:14.2%">TEPS</th>
                        <th style="border-right :1px solid #cccccc; width:14.2%">New TEPS</th>
                        <th style="border-right :1px solid #cccccc; width:14.2%">OPIc</th>
                        <th style="border-right :1px solid #cccccc; width:14.2%">TOEIC Speaking</th>
                        <th style="border-right :1px solid #cccccc; width:14.2%">초과학기</th>
                        <th style="width:14.2%">Intensive English</th>
                    </tr>
                    <tr class="mytr">
                        <td class="mytd">700점 이상</td>
                        <td class="mytd">80점 이상</td>
                        <td class="mytd">556점 이상</td>
                        <td class="mytd">301점 이상</td>
                        <td class="mytd">Intermediate IL 이상</td>
                        <td class="mytd">120점 이상</td>
                        <td class="mytd">2학기 이상 면제</td>
                        <td class="mytd" style="border-right :0px">과목 이수</td>
                    </tr>
                </table>
                <div class="partdiv">
                    
                    <span style="color:#17a55e">
                        위 조건을 만족하였습니다
                        
                            
                            <br><br>
                            <span style="font-size:1.2rem;">- 내 점수 : </span>
                            <span style="font-weight: bold;">OPIc / IH</span>
                            
                        </span>

                </div>
            </div>
        </div>
    </div>
</div>




    <!--footer-->
    <footer class="footer">
        <ul class="footer_list">
            <li>
                - Contact -
            </li>
            <li>
                Email : hanjo8813@gmail.com
            </li>
            <li>
                GitHub : <a href='https://github.com/hanjo8813/PleaseGraduate' style='color:lightgrey'
                    target='_blank'>https://github.com/hanjo8813/PleaseGraduate</a>
            </li>
        </ul>
        <h2 class="copyright">Copyright
            <i class="far fa-copyright"></i>
            2021 PleaseGraduate team <br>
            강전호, 강홍구, 권정현, 안재현, 한재원
        </h2>
    </footer>



    
    <!-- 주의사항 버튼 -->
    <div class="info_btn" onclick='pop_info_modal()'>
        <i class="fas fa-question"></i>
    </div>

    <!-- 주의사항 모달 -->
    <div id="info_modal" class="modal">
        <div class="modal-content" style='width:80%'>
            <span class="close" onclick='close_info_modal()'>&times;</span>
            <div class="container" style='padding:0 1rem 0 1rem; '>

                <!-- 과목 관련 -->
                <div class="info_title">도움말</div>
                <div class="info_box">
                    <div class="info_content">
                        <p>1. 각 영역별 졸업요건 만족 조건을 잘 모르겠다면 검사 결과창에서 <b>Tip</b> 버튼을 눌러보세요!</p>
                        <p>2. 타학과 전공 인정과목은 학교에서 처리하기 전까지 엑셀파일에 <b>'교양'</b>으로 기재됩니다. 추후 학교측에서 이수구분을 전공으로 변경합니다.</p>
                        <p>3. <b>English Listening Practice 1</b> 혹은 <b>대학영어</b> 과목을 이수면제 받은 사용자는 아래의 절차를 통해
                            해당 과목을 추가할 수 있습니다.</p>
                        <p style="margin-left:1rem; font-size:0.85rem;">
                            - 커스텀기능 > 학수번호에 "면제" 검색 > 출력된 ELP1/대학영어 커스텀 과목 추가 (0학점짜리)
                        </p>
                        <p>4. <span class="caution_info">Please Graduate의 고전독서인증현황과 기이수과목은 자동으로 업데이트 되지 않습니다.</span></p>
                        <p style="margin-left:1rem; font-size:0.85rem;">
                            - 고전독서인증현황에 변동이 있을 경우, 대양휴머니티칼리지 > 나의 인증현황 메뉴에서 변경 확인 후 마이페이지에서 업데이트하시길 바랍니다.
                        </p>
                        <p style="margin-left:1rem; font-size:0.85rem;">
                            - 학기가 끝난 후, 학사정보시스템에서 기이수성적표가 완성되면 마이페이지에서 엑셀을 새로 업로드하시길 바랍니다.
                        </p>
                    </div>
                </div>

                <!-- 검사관련 박스 -->
                <div class="info_title">검사 관련</div>
                <div class="info_box">
                    <div class="info_content">
                        <p>1. <b>복수전공</b> 기준은 복필-15학점, 복선-24학점 / 주전공 전필-15학점, 전선-24학점으로 설정되어 있습니다.</p>
                        <p style="margin-left:1rem; font-size:0.85rem;">
                            ※ 법학과, 건축학과, 항공시스템공학과, 국방시스템공학과 복전 등의 특수한 경우는 기준학점이 다르며, 반영되지 않았습니다.
                        </p>
                        <p>2. <b>연계·융합전공</b> 기준은 연선-15학점, 연필-24학점 / 주전공 전필-15학점, 전선-24학점으로 설정되어 있습니다.</p>
                        <p>3. 복수/연계 <b>부전공</b>에 대한 기준은 설정되지 않았습니다. 이를 유의하시기 바랍니다.</p>
                        <p>4. 추천 과목 정보는 2022-1, 2022-2학기 정보로, 최신 기준으로 제공됩니다. (ex. 과거엔 서양철학이 2학점이였다면 현재는 3학점으로 변경됨)</p>
                        <p>5. 검사 기준은 최신버전 수강편람(2022.08.10)을 반영하여 설정되었으며, 수강편람은 매년 개편되므로 자신이 알고 있는 구버전 수강편람과 다를 수 있습니다.
                        </p>
                        <p style="margin-left:1rem; font-size:0.85rem;">- 세종대학교 교과과정 참고 링크 : &nbsp;&nbsp;
                            <a class="link_site" target="_blank"
                            href="http://board.sejong.ac.kr/boardview.do?pkid=156096&currentPage=1&searchField=ALL&siteGubun=19&menuGubun=1&bbsConfigFK=335">
                            수강편람</a>
                            &nbsp;&nbsp;
                            <a class="link_site" target="_blank"
                                href="http://abeek.sejong.ac.kr/abeek/program0501.html">공학인증</a>
                        </p>
                        <p>6. 세종대학교에서 공식적으로 만든 사이트가 아니므로 <span class="caution_info">검사 결과가 정확하지 않을 수 있습니다.</span> (반드시 수강편람을 통한 졸업요건 2차 검증을 해야합니다.)</p>
                        <p>7. 졸업요건 기준이 잘못 설정되었거나, 오류발생 시 상단 메뉴바링크로 피드백 부탁드립니다.</p>
                    </div>
                </div>

                <!-- 안내사항 박스 -->
                <div class="info_title">안내 사항</div>
                <div class="info_box">
                    <div class="info_content">
                        <p>1. 비밀번호 찾기 및 내정보 업데이트 사용시&nbsp;
                            <a class="link_site" target="_blank" href="https://portal.sejong.ac.kr/">세종대학교포털</a>
                            사이트에서 개인정보수집 동의가 되어있어야합니다. (보통 동의되어있음)
                        </p>
                        <p style="margin-left:1rem; font-size:0.85rem;">- 로그인 -> 정보수정 -> 개인정보수집동의 모두 동의</p>
                        <P>2. 내정보 업데이트 시&nbsp;
                            <a class="link_site" target="_blank" href="http://classic.sejong.ac.kr/">대양휴머니티칼리지</a>
                            사이트에서 학생 기본 정보와 고전독서의 영역별 인증 현황을 가져옵니다.
                        </P>
                        <p style="margin-left:1rem; font-size:0.85rem;">- 고전독서인증 : 대양휴머니티칼리지 -> 고전독서인증센터 -> 영역별 인증현황</p>
                        <p>3. 사용자의 세종대학교 포털 사이트의 비밀번호는 인증에만 1회 사용되며 <span class="caution_info">저장되지 않습니다.</span></p>
                        <p>4. 검사를 위해선 기이수성적 엑셀파일을 직접 업로드해야하므로 <span class="caution_info">PC환경</span>에서 진행하는 것을 권장합니다.
                        </p>
                        <p>5. 사용자가 업로드하는 기이수성적 엑셀파일은 <span class="caution_info">저장되지 않고,</span> 평점을 제외한 과목정보만이 데이터베이스로
                            변환하여 저장됩니다.</p>
                        <p>6. 업로드 시 성적 중 평점이 <span class="caution_info">F, NP인 과목은 인정되지 않고 자동 삭제됩니다.</span></p>
                        <p>7. 저장된 사용자 데이터베이스는 <span class="caution_info">과목추천 및 교양과목 통계</span>에만 사용되며, 다른 용도로 사용되지 않습니다.
                        </p>
                    </div>
                </div>
            </div>
            <div style="text-align: center;">
                <button onclick="close_info_modal()" class="suc_btn" style="letter-spacing: 5px;">닫기</button>
            </div>
        </div>
    </div>
    

    <!-- 업데이트 성공 모달 -->
    

    <!-- 사용금지 모달
    <div id='myModal_stop' class="modal" style ="display: block;">
        <div class="modal-content">
            <div class="modal_div">
                <div style="font-size:2.5rem; font-weight:bold; color : #d32f2f">
                    ※ 사이트 점검 중입니다. ※
                </div>
                <div style="font-size:1.3rem; margin-top:3rem;">
                    <p style="font-size:2rem; font-weight:bold;">~ 01:00 까지 점검 예정입니다.</p>
                </div>
            </div>
        </div>
    </div>-->
</body>




<!-- 원그래프 js 참조 -->

<script src="/static/js/circle-progress.js"></script>
<script src="/static/js/modal.js"></script>

<script>
    // 결과창에서 뒤로가기 버튼 클릭시 무조건 mypage로
    history.pushState(null, null, location.href);
    window.onpopstate = function (event) {
        window.location.href = '/mypage/';
    };

    // 퍼센트화 함수
    function to_percent(my, standard) {
        a = (my / standard) * 100
        if (a > 100) {
            a = 100
        }
        return a;
    }

    // 데이터 바인딩

    // 사용자 정보
    var Studentnumber = '17010816';
    var Name = '김준영';
    // 기준학점
    var Totalgrade = '130';               // 총학점
    var Grade1 = '15';         // 전필
    var Grade2 = '24';         // 전선
    // 사용자 학점
    var Mytotalgrade = '85';         // 총학점
    var Mygrade1 = '15'    // 전필
    var Mygrade2 = '12'    // 전선
    var remain = '3'        // 전필 초과 학점
    // 인증권수
    var Swbook = 0;
    var Wbook = 0;
    var Sbook = 0;
    var Scbook = 0;
    var Mybook = 10;
    if ('0' != 2) {
        Swbook = '3' + "권";
        Wbook = '4' + "권";
        Sbook = '0' + "권";
        Scbook = '1' + "권";
        Mybook = '6';
    }

    // 이수 학점 퍼센트화
    var pernum0 = to_percent(Mytotalgrade, Totalgrade); // 총학점
    var pernum1 = to_percent(Mygrade1, Grade1);         // 전필
    var pernum2 = to_percent(Number(Mygrade2) + Number(remain), Grade2);         // 전선
    var pernum7 = to_percent(Mybook, 10);               // 고전독서

    // pass 여부
    // 총 검사 결과
    if (pernum0 >= 100) {
        if ('0' == 1) {
            var Cangraduate = "축하합니다! 졸업 가능합니다!";
            document.querySelector('.T').style.fontSize = '24px';
        }
        // 학점은 만족하나 조건이 안될 경우
        else {
            pernum0 = 99;
            document.querySelector('.cap').style.display = 'none';
            document.querySelector('.T').style.fontSize = '23px';
            var Cangraduate = "영역 기준을 모두 만족하지 못했습니다.";
        }
    } else {
        document.querySelector('.cap').style.display = 'none';
        document.querySelector('.T').style.fontSize = '23px';
        var Cangraduate = "총 기준학점보다 " + (Totalgrade - Mytotalgrade) + "학점이 부족합니다!";
    }
    // id값과 매핑
    document.getElementById("name").innerHTML = Name;
    document.getElementById("studentnumber").innerHTML = Studentnumber;
    document.getElementById("grade1").innerHTML = Grade1;
    document.getElementById("grade2").innerHTML = Grade2;
    document.getElementById("mygrade1").innerHTML = Mygrade1;
    document.getElementById("mygrade2").innerHTML = Mygrade2;
    if (remain != 0) {
        document.getElementById("myremain").innerHTML = '+' + remain;
    }
    document.getElementById("mytotalgrade").innerHTML = Mytotalgrade;
    document.getElementById("totalgrade").innerHTML = Totalgrade;
    document.getElementById("cangraduate").innerHTML = Cangraduate;
    document.getElementById("swbook").innerHTML = Swbook;
    document.getElementById("sbook").innerHTML = Sbook;
    document.getElementById("wbook").innerHTML = Wbook;
    document.getElementById("scbook").innerHTML = Scbook;


    // 차트 함수
    var CircleProgress = function (x, y, z) {
        if (x == 100) {
            $(y)
                .circleProgress({
                    value: x / 100,
                    startAngle: 300,
                    size: z,
                    animation: {
                        duration: 2200,
                        easing: "swing"
                    },
                    thickness: 15,
                    fill: {
                        gradient: ["#9ae6b3", "#6aa87f"]
                    }
                })
                .on('circle-animation-progress', function (event, progress, stepValue) {
                    $(this)
                        .find('strong')
                        .html(Math.round(x * progress) + '<i>%</i>');
                });
        } else {
            $(y)
                .circleProgress({
                    value: x / 100,
                    startAngle: 300,
                    size: z,
                    animation: {
                        duration: 2200,
                        easing: "swing"
                    },
                    thickness: 15,
                    fill: {

                        gradient: ["#f5aeb0", "#b06163"]
                    }
                })
                .on('circle-animation-progress', function (event, progress, stepValue) {

                    $(this)
                        .find('strong')
                        .html(Math.round(x * progress) + '<i>%</i>');
                });
        }
    }
    CircleProgress(pernum0, '#chart0', 250);
    CircleProgress(pernum1, '#chart1', 150);
    CircleProgress(pernum2, '#chart2', 150);
    CircleProgress(pernum7, '#chart7', 150);
    

    var modal1 = document.getElementById('myModal1');
    var modal2 = document.getElementById('myModal2');

    var btn1 = document.getElementById("myBtn1");
    var btn2 = document.getElementById("myBtn2");
    
    var span1 = document.getElementById("close1");
    var span2 = document.getElementById("close2");

    Btnclick(btn1, modal1);
    Btnclick(btn2, modal2);

    Spanclick(span1, modal1);
    Spanclick(span2, modal2);

    // 툴팁 함수
    let tooltip_btn = document.querySelectorAll('.tooltip');
    let tooltip_box = document.querySelectorAll('.tooltip_text');
    window.onload = function(){

        for (i = 0; i < tooltip_btn.length; i++) {
            Tooltipeb(tooltip_btn[i], tooltip_box[i]);
        }

        function Tooltipeb(btn, box) {
            btn.addEventListener('click', () => {
                box.classList.toggle('active');
            });
        }
    }
    
    // 모달 밖 클릭시 꺼짐 함수
    window.onclick = function (event) {

        if (event.target == modal1) {
            modal1.style.display = "none";
        }
        if (event.target == modal2) {
            modal2.style.display = "none";
        }
        if (typeof modal3 !== 'undefined') {
            if (event.target == modal3) {
                modal3.style.display = "none";
            }
        }
        if (typeof modal4 !== 'undefined') {
            if (event.target == modal4) {
                modal4.style.display = "none";
            }
        }
        if (typeof modal5 !== 'undefined') {
            if (event.target == modal5) {
                modal5.style.display = "none";
            }
        }
        if (typeof modal8 !== 'undefined') {
            if (event.target == modal8) {
                modal8.style.display = "none";
            }
        }
    }

</script>



<script>
    // 교필 영역 함수
    var Grade3 = '7';
    var Mygrade3 = '6';
    var pernum3 = to_percent(Mygrade3, Grade3);

    document.getElementById("grade3").innerHTML = Grade3 + "개";
    document.getElementById("mygrade3").innerHTML = Mygrade3 + "개";
    var modal3 = document.getElementById('myModal3');
    var btn3 = document.getElementById("myBtn3");
    var span3 = document.getElementById("close3");
    Btnclick(btn3, modal3);
    Spanclick(span3, modal3);

    CircleProgress(pernum3, '#chart3', 150);
</script>




<script>
    // 교선 영역 함수
    var Grade4 = '15';
    var Mygrade4 = '10';
    var pernum4 = to_percent(Mygrade4, Grade4);
    // 선택영역 패스여부
    var Myarea4;
    if ('1' == 1) {
        Myarea4 = "Pass";
    }
    else {
        Myarea4 = "NP";
        if (pernum4 == 100) {
            pernum4 -= 1;
        }
    }
    // 필수과목 패스여부
    var Cs_p;
    if ('1' == 1) {
        Cs_p = "Pass";
    }
    else {
        Cs_p = "NP";
        if (pernum4 == 100) {
            pernum4 -= 1;
        }
    }
    document.getElementById("grade4").innerHTML = Grade4;
    document.getElementById("myarea4").innerHTML = Myarea4;
    document.getElementById("mygrade4").innerHTML = Mygrade4;
    document.getElementById("cs_p").innerHTML = Cs_p;
    var modal4 = document.getElementById('myModal4');
    var btn4 = document.getElementById("myBtn4");
    var span4 = document.getElementById("close4");
    Btnclick(btn4, modal4);
    Spanclick(span4, modal4);

    CircleProgress(pernum4, '#chart4', 150);
</script>







<script>
    // 기교 영역 함수
    var Grade5 = '6';
    var Mygrade5 = '6';
    var pernum5 = to_percent(Mygrade5, Grade5);

    // 화학과 기교 걸러내기
    if ('전자정보통신공학과' == '화학과') {
        b_p = ''
        if (b_p == 1) {
            pernum5 = 100;
        }
        else {
            if (pernum5 == 100) {
                pernum5 -= 1;
            }
        }
    }
    
    document.getElementById("grade5").innerHTML = Grade5 + "개";
    document.getElementById("mygrade5").innerHTML = Mygrade5 + "개";
    var modal5 = document.getElementById('myModal5');
    var btn5 = document.getElementById("myBtn5");
    var span5 = document.getElementById("close5");
    Btnclick(btn5, modal5);
    Spanclick(span5, modal5);

    CircleProgress(pernum5, '#chart5', 150);
</script>




<script>
    // 영어인증
    if ('1' == 1) {
        var Grade8 = "Pass";
        var pernum8 = 100;
    }
    else {
        var Grade8 = "NP";
        var pernum8 = 0;
    }

    document.getElementById("grade8").innerHTML = Grade8;
    var modal8 = document.getElementById('myModal8');
    var btn8 = document.getElementById("myBtn8");
    var span8 = document.getElementById("close8");
    Btnclick(btn8, modal8);
    Spanclick(span8, modal8);

    CircleProgress(pernum8, '#chart8', 150);
</script>




<script>
    // 연계/복수전공시 차트 함수
    var Grade_multi_me = '15';
    var Grade_multi_ms = '24';
    var Mygrade_multi_me = '6';
    var Mygrade_multi_ms = '6';
    var multi_remain = '0';

    var pernum_multi_me = to_percent(Mygrade_multi_me, Grade_multi_me);
    var pernum_multi_ms = to_percent(Number(Mygrade_multi_ms) + Number(multi_remain), Grade_multi_ms);

    document.getElementById("grade_multi_me").innerHTML = Grade_multi_me;
    document.getElementById("grade_multi_ms").innerHTML = Grade_multi_ms;
    if (multi_remain != 0) {
        document.getElementById("multi_remain").innerHTML = '+' + multi_remain;
    }
    document.getElementById("my_grade_multi_me").innerHTML = Mygrade_multi_me;
    document.getElementById("my_grade_multi_ms").innerHTML = Mygrade_multi_ms;

    CircleProgres