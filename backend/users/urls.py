from django.urls import path
from .views import (
    MyInfo,
    LogIn,
    LogOut,
    Users,
    PublicUser,
    CheckUserExist,
    GithubRegister,
    GithubLogIn,
)


urlpatterns = [
    # 사용자 목록조회
    path("", Users.as_view()),
    # 로그인한 사용자 정보 조회
    path("myinfo", MyInfo.as_view()),
    # 로그인 -> 세션, token
    path("log-in", LogIn.as_view()),
    # 로그아웃 -> 만료
    path("log-out", LogOut.as_view()),
    # 사용자 존재여부 확인
    path("check-user-exist", CheckUserExist.as_view()),
    # 깃허브 로그인
    path("github-log-in", GithubLogIn.as_view()),
    # 깃허브 등록
    path("github-register", GithubRegister.as_view()),
    # 공개 계정 조회
    path("@<str:username>", PublicUser.as_view()),
]
