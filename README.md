# :deciduous_tree: 산넘고 산넘어

<pre>
  4일동안 진행된 미니 프로젝트로 전국의 산을 소개합니다.
  등산을 사랑하는 사람들이 등산 후기와 산의 정보를 공유할 수 있는 사이트 입니다. 
</pre>

## Stack

### Frontend

-   HTML
-   CSS (Bulma)
-   JavaScript

### Backend

-   Flask, MongoDB Atlas

### 배포

- AWS EC2

## Product

[유튜브](https://youtu.be/ScFCljhbfw0)

[산넘고 산넘어](whatiwant-karma.shop)

# 역할

## Member

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/shippig"
        ><img
          src="https://avatars.githubusercontent.com/u/42665042?v=4"
          width="100px;"
          alt=""
        /><br /><sub><b>인상운</b></sub></a
      ><br />
    </td>
    <td align="center">
      <a href="https://github.com/coldrain-f"
        ><img
          src="https://avatars.githubusercontent.com/u/81298415?v=4"
          width="100px;"
          alt=""
        /><br /><sub><b>황윤정</b></sub></a
      ><br />
    </td>
    <td align="center">
      <a href="https://github.com/beomjin96"
        ><img
          src="https://avatars.githubusercontent.com/u/102977561?v=4"
          width="100px;"
          alt=""
        /><br /><sub><b>김범진</b></sub></a
      ><br />
    </td>
    <td align="center">
      <a href="https://github.com/gureumwoon"
        ><img
          src="https://avatars.githubusercontent.com/u/83581867?v=4"
          width="100px;"
          alt=""
        /><br /><sub><b>김채운</b></sub></a><br />
    </td>
  </tr>
</table>

## Page UI 및 기능 구현

| 이름       | pages                                                                            |
| ---------- | -------------------------------------------------------------------------------- |
| **인상운** | 로그인, 로그아웃, 게시물 수정, 게시물 삭제                           |
| **김채운** | 회원가입                           |
| **김범진** | 메인페이지, 상세보기     |
| **황윤정** | 게시물 업로드|

# 상세 기능

<h2>로그인 (인상운)</h2>

<table>
  <tr align="center">
    <td align="center">
        <img
          src="https://user-images.githubusercontent.com/83581867/168465262-52de9e0f-f098-4cd9-963d-1034288d61f3.gif"
          width="400px;"
          alt=""
        /><br/><sub><b>로그인 성공</b></sub><br />
    </td>
     <td align="center">
        <img
          src="https://user-images.githubusercontent.com/83581867/168465320-abd0d4bd-ed51-4916-bfa9-b377c7f3ae84.gif"
          width="400px;"
          alt=""
        /><br /><sub><b>로그인 실패</b></sub><br />
    </td>
  </tr>
</table>

- 로그인 페이지는 JWT 토큰을 사용해 기능을 구현했습니다.
- '로그인' 버튼을 클릭하면 이메일 주소와 비밀번호에 대한 유효성 검사를 진행하고, 이메일 주소와 비밀번호가 일치하지 않으면 알림창으로
  '이메일과 비밀번호가 일치하지 않습니다.' 라는 경고문구가 나타납니다.
  
<h2>회원가입 (김채운)</h2>

<table>
  <tr align="center">
    <td align="center">
        <img
          src="https://user-images.githubusercontent.com/83581867/168467154-056f4a99-0b16-4dc5-9724-9547886b7d30.gif"
          width="400px;"
          alt=""
        /><br/><sub><b>중복검사</b></sub><br />
    </td>
     <td align="center">
        <img
          src="https://user-images.githubusercontent.com/83581867/168467189-e9e96fdc-2772-4f69-87ca-1b50c3d4189a.gif"
          width="400px;"
          alt=""
        /><br /><sub><b>유효성검</b></sub><br />
    </td>
  </tr>
</table>

- 회원가입 할 이메일과 비밀번호는 중복검사 버튼을 통해서 사용이 가능한지 불가한지 검사 해줍니다.
- 회원가입 버튼을 클릭하면 이메일과 닉네임 형식이 올바른지, 비밀번호와 비밀번호 확인란에 입력한 게 일치하는지, 닉네임 형식이 올바른지 전체적인 유효성 검사를 해주고, 빈칸이거나 이메일(@), 비밀번번호(영문과 숫자 필수 포함, 특수문자(!@#$%^&*)사용가능 8-20자)이 유효하지 않거나, 닉네임(2-10자의 영문과 숫자와 일부 특수문자(._-)만 입력 가능합니다.) 등의 형식이 맞지 않으면 입력창 밑에 경고문이 뜹니다.
  
<h2>게시물 등록 (황윤정) & 메인페이지 (김범진)</h2>

  <div align="center">
      <img
         src="https://user-images.githubusercontent.com/83581867/168472003-faa447d6-ea31-4c90-a70d-868d6c4532f1.gif"
         width="500px;"
         alt=""
       />
  </div>
  
  - 메인페이지에서 글쓰기 버튼을 클릭하면 게시물 등록 페이지가 나옵니다.
  - 제목, 산 이름, level, 이미지 본문을 입력하고 '등록' 버튼을 누르면 메인페이지로 이동하고 메인페이지 게시물 리스트에 글이 등록된 걸 확인 할 수 있습니다.

<h2>게시물 수정 (인상운) & 상세보기,지메인페이지 (김범진)</h2>

 <div align="center">
      <img
         src="https://user-images.githubusercontent.com/83581867/168472240-de5766c8-7358-420f-a97a-84f922fcd0b5.gif"
         width="500px;"
         alt=""
       />
  </div>
  
  - 메인페이지에서 게시물에 상세보기를 클리하면 상세보기 페이지로 이동합니다.
  - '수정' 버튼을 클릭하면 수정 페이지로 이동 합니다.
  - 게시물이 그대로 가져와지고 그 상태에서 제목, 산 이름, 이미지, 본문 글을 수정하고 '수정' 버튼을 클릭하면 수정된 상태로 메인페이지에 게시물이 업데이트 된 걸 확인할 수 있습니다.

<h2>게시물 삭제 (인상운) & 상세보기,메인페이지 (김범진)</h2>

  <div align="center">
      <img
         src="https://user-images.githubusercontent.com/83581867/168472134-1eaa5706-a017-4fbe-aa8a-0bc7c3c31d4a.gif"
         width="500px;"
         alt=""
       />
  </div>
  
  - 메인페이지에서 게시물에 상세보기를 클리하면 상세보기 페이지로 이동합니다.
  - '삭제' 버튼을 클릭하면 메인페이지로 이동하고 메인페이지 게시물 리스트에서 삭제가 된 걸 확인 할 수 있습니다.

<h2>로그아웃 (인상운)</h2>

  <div align="center">
      <img
         src="https://user-images.githubusercontent.com/83581867/168472095-897ef649-d9b2-47a6-ac3e-062029d6ec5f.gif"
         width="500px;"
         alt=""
       />
  </div>
  
  - 페이지 상단 메뉴에서 '로그아웃' 버튼을 클릭하면 로그아웃이 되고 로그인 페이지로 이동합니다.
