# ESW-TankGame-Fury-
ESW project - tank game

-시연 영상

https://youtu.be/fSwk3gUgC5Q

## 배경

![71wRqdhqLpL](https://github.com/user-attachments/assets/88241c06-5ecd-4377-aa29-0c2f6ff77823)

게임의 배경은 2차 세계대전 전차 승무원의 이야기를 다룬 영화인 "Fury"에 영감을 받아 "직접 전차를 운용하는 승무원이 되어보자!"는 게임을 만들게 되었습니다.
게임의 배경은 2차 세계 대전중 독일에서 작전하고있는 미군 전차병의 시점이 됩니다.
플레이어는 당시 미군이 주력으로 운용하였던 M4 셔먼 전차를 운용하여 적 전차를 격파해 나가면됩니다.



## 아이디어

**1. 게임의 주요 아이디어**

게임 장르: 2D 슈팅 게임

이 게임은 플레이어가, 인 게임상의 전차 운용병이 되어 전차를 조작하여 모든 적 전차를 처치하는 게임입니다.
플레이어의 주된 목표는 최대한 전차에 피해를 입지않으면서 적 전차를 모두 파괴해야합니다.

**2. 게임의 주요 요소**

게임상의 주요 오브젝트로는, 플레이어와 적군이 있으며
플레이어는 전차를 운용하는 운용병이 되며, 전차를 적절히 운용하여 적군과의 전투에서 최대한의 체력손실없이 승리해야됩니다.
기본적으로 플레이어 전차는 M4 셔먼으로, 2차세계대전당시 미군의 주력전차입니다. 전차를 조작키를 이용해 좌-우로 기동하며, 포신의 각도를 조절해 포탄의 낙차에 맞게 적군을 정확히 조준한 후 발사해야됩니다. 그래야 적 전차에게 명중탄을 맞출수 있습니다.
적 전차에게 명중탄을 맞추면 포탄이 터지는 애니메이션이 나오며 게임에 몰입감을 줍니다.

**3. 게임의 도전과 재미 요소**

기본적으로, 게임에서 플레이어가 포탄을 적 전차에 맞추려면 플레이어와 적 전차간의 거리를 고려해서 포신의 각도를 조절해야하며,
피해를 입지않기위해 최대한 빠르게 포탄을 쏘고 기동을 해서 적의 포탄을 피해야 될겁니다.
위와 같은 과정들을 플레이어가 직접 시도해봄으로써 플레이어는 적들을 해치워 나가며 즐거움을 느낄겁니다. 

**4. 게임의 장기적 목표 또는 확장 가능성**

현재 게임에 구현되어있는 내용은, 단순하게 1스테이지에서 기본적인 전차를 가지고 기본적인 적들을 격파해나가는 방식입니다.
변칙성을 추가하기 위해서, 플레이어가 전차를 업그레이드 할수있는 기능이나 (예를들어, 전차의 속도, 전차의 포탄 데미지, 전차의 장전속도)등을 구현하고
현재 지형의 경우 지형이 밋밋한 평지이지만 곡선형 지형을 추가해 포탄을 발사하는데 있어 많은 변수들을 추가하고싶습니다.
적들도 현재 한가지로 통일되어있지만, 추후 여러 다양한 무기들을 사용하는 적들을 만들어, 피탄면적이 작은적이나, 아니면 유도무기를 사용하는 적을 추가할 생각입니다.

또한 하드웨어 적으로 업그레이드를 염두에 두고있는데, 현재는 포신의 각도조절을 위해 USB 조이스틱을 사용하고있습니다. 이 USB 조이스틱에는 게임에서 할당할수있는 많은 조작키들을 보유하고있는데 이를 특수무장이나, 세부조작을 위해 추가하면 좋을것으로 생각됩니다.



-SMB 디렉토리 활용
-USB 조이스틱 활용
-케이스 직접제작

## 게임방법
### 1. 게임 시작
- 게임이 시작되면 화면에 전차가 공중에 스폰되며, 전차가 지형에 내려앉으면 게임이 시작됩니다.
- 플레이어어가 직접적으로 조작이 가능한 키는, 라즈베리파이에 직접적으로 연결되어있는 게임패드 와 추가적으로 USB 조이스틱을 이용해 게임을 조작할수있습니다

**- 기본 조작방식**
![그림1](https://github.com/user-attachments/assets/0d156dfa-4314-471b-a4e7-d9561ef1de6d)

먼저 기본적인 조이스틱을 이용한 조작방법입니다. 조작 가능한 키는 아래와 같습니다

**1. 조이스틱 좌측 방향키**

  게임이 실행되고 좌측 방향키를 누르면 캐릭터(전차)는 왼쪽으로 기동합니다.

**2. 조이스틱 우측 방향키**

  게임이 실행되고 우측 방향키를 누르면 캐릭터(전차)는 오른쪽으로 기동합니다.

**3. 조이스틱 하단 방향키**

  만약 게임을 하다 캐릭터의 체력이 0이되어 죽거나, 모든 적을 격파하면 "승리" 나 "패배" 화면이 출력되는데 이때 조이스틱 하단키를 누르면 게임이 재시작됩니다.

**4. 조이스틱 오른쪽 A 버튼키**

  A 버튼을 누르면 캐릭터가 활성화 되어있을때 캐릭터(전차)의 포신에서 포탄이 발사됩니다.

--------------

**- 조이스틱을 사용한 조작방식**
![그림2](https://github.com/user-attachments/assets/51582e5b-8d6d-47eb-9092-9e6cef962de7)

다음은 USB 조이스틱을 별도로 연동해서 사용하는 조작방식입니다. 조작가능한 키는 아래와 같습니다

**1. y축 스틱조작**

  y축으로 스틱을 조작하면 포신의 부양각이 변합니다. 아래쪽으로 당기면 포신이 상승하고, 위쪽으로 당기면 포신이 하강합니다.

**2. 스틱 버튼 0번**

  스틱의 0번 버튼(트리거)를 누르면 포신에서 포탄이 발사됩니다. 기본 조이스틱 오른쪽 A 버튼키와 로직은 동일합니다.

--------------

### 2. 캐릭터 이동

플레이어는 랜더링된 지형, 화면 내에서 캐릭터를 좌우로 이동시킬수있으며, 만약 USB 조이스틱을 사용한다면 포신의 부양각도 조절할수있습니다.
게임은 횡스크롤 방식으로 되어있으며, 좌-우 스틱을 누르면 X 좌표값이 변하며 캐릭터가 이동합니다.
캐릭터는 이동할때 2프레임 애니메이션을 재생하게 되어있어 실제 이동하는 듯한 느낌을 받을수있습니다.

### 3. 포탄 발사

플레이어는 A 버튼과, USB 조이스틱의 0번 버튼을 누름으로써 포탄을 발사할수있습니다.
포탄이 발사되는 위치의 경우 포신의 끝단에서 발사됩니다. 기본적인 offset은 수평으로 유지하고있어 오른쪽 방향으로 직사가 가능합니다.
포탄은 중력의 영향을 받아서 포물선을 그리며 떨어지기에 플레이어는 이를 감안하여 발사하여 맞출수있는 거리를 잘 산정해야됩니다
만약 USB 조이스틱을 사용한다면 포신의 부양각을 조절할수있기에 더욱 다채로운 플레이가 가능합니다.
또한, 포탄이 지형이나, 적, 캐릭터에 부딛힐경우 터지는 애니메이션이 구현되어있기에 더욱 생동감 있는 플레이가 가능합니다.

### 4. 적군의 등장

플레이어가 스폰된 맵에는 적군이 구현되어있습니다.
이 게임의 전략적 목표는 맵상의 모든 적들을 처치하는게 목표입니다.
적군은 일정 간격으로 플레이어에게 10씩 데미지를 주는 포탄을 발사합니다. (플레이어는 총 체력 100을 가지고있습니다.)
플레이어는 체력 100이 다 없어지기전에 맵의 모든 적들을 격파해야합니다.
또한 적군의 체력의 경우, 플레이어가 발사한 포탄에 맞으면 바로 사라지도록 구현되어있습니다.
(더 개발을 한다면 추후 적군을 다양하게 추가할 생각입니다.)

### 5. 체력 바와 UI

화면 중앙에는 플레이어의 체력바가 표시됩니다. 이를 통해 플레이어의 체력이 얼마나 남아있는지 직관적으로 알수있습니다.
처음에는 빨간색 막대기로 꽉 채워져있다가. 플레이어가 피해를 입으면 빨간색 막대기가 줄어듭니다. 만약 0이면되면 이 막대기가 다 사라지겠죠?

### 6. 게임 종료 조건

게임이 종료되는 조건은 간단합니다. 플레이어가 스폰되는 맵의 모든 적을 죽이던가, 아니면 플레이어가 죽던가 2가지입니다.


## 사용된 기술

사용한 라이브러리를 나열하면 아래와 같습니다.

**1. PIL 라이브러리**

PIL 라이브러리의 주요 사용처는 이미지를 로드, 리사이징, 화면에 랜더링하는것이 주된 역할입니다.
화면에 띄워지는 캐릭터, 적군, 지형, 배경, 탄, 체력바, 애니메이션 모두 PIL 라이브러리에 기반하고있습니다.
또한 "패배" 나 "승리" 화면 모두 PIL 라이브러리로 구현, 랜더하고있습니다.

**2. Numpy 라이브러리**

수학적 계산을 담당하는 라이브러리 입니다. 
캐릭터가 이동할때 적군, 배경, 지형, 적군, 포탄 등의 좌표값을 관리해야하며, 배열 관리또한 담당하고있습니다.
또한 만약 좌표값끼리 일치하거나, 일정 범위값 아래로 내려가게되면 충돌하게 된것으로 판정을 내리며, 이를통해 적군이나 캐릭터의 체력을 줄이는 역할을 하고있습니다.

**3. pygame 라이브러리**

pygame 라이브러리는 교수님께서 조이스틱 컨트롤에 한정해서 허가하셔서 사용하였습니다.
pygame 라이브러리의 역할은 단 1가지입니다. USB 조이스틱에서 스틱의 축값을 import 해오는 역할입니다.
이 import 해온 축값을 통해 포신의 각도를 컨트롤 할수있었습니다.

**4. Time 라이브러리**

시간에 관련된 라이브러리입니다.
게임 전체적인 루프에서 딜레이를 구현하며, 적군이 포탄을 장전하고 발사하는 딜레이 시간을 관리하는 역할을 했습니다.

**- 이외에도 사용된 기술 (소프트웨어 및 하드웨어)**

**1. 객체 지향 프로그래밍**

Python의 경우 객체지향 프로그래밍이 가능한데, 게임의 요소 캐릭터, 적군, 총알 등... 을 클래스로 정의하고, 이들 간의 상호작용을 처리하는 기술을 적용했습니다.

**2. 충돌 감지 알고리즘**

2D 충돌 감지 알고리즘을 사용하여 객체 간 충돌을 확인하는 알고리즘을 구현했습니다.
현재 게임에 구현되어있는 충돌효과가 있는 obj의 경우 지형, 캐릭터, 적군, 총알입니다.
overlap() 메서드를 통해 두 객체의 경계 가 겹치는지 확인하고 충돌 여부를 반환합니다.
collision_check()에서 overlap()을 활용하여 총알이 적군이나 캐릭터와 충돌하는지 판단하고, 충돌 시 상태 변경과 체력 감소를 처리합니다.

**3. 애니메이션 처리**

폭발 애니메이션과 같은 동적 이미지 처리를 위해 여러 이미지 프레임을 순차적으로 표시하는 방식입니다.
예를 들어 총알의 경우, "폭발" 상태가 될경우 애니메이션이 재생되는데, 1프레임마다 파일에있는 이미지를 변환해가며 출력합니다.

**4. 2D 물리 엔진 (Gravity, Velocity)**

2D 물리 엔진을 간단하게 구현하여 중력과 속도를 처리합니다.
총알의 궤적을 계산할 때 중력의 영향을 고려하여 move() 메서드에서 self.velocity_y와 self.gravity를 통해 총알의 y 위치를 계산합니다.
중력 적용을 위해 0.5 * self.gravity * (self.time ** 2)의 물리 공식을 사용했습니다.

**5. 라즈베리 파이 본체**

![캐드설계](https://github.com/user-attachments/assets/3605c9a7-b20d-4764-afa7-1e7d60e4d0d0)

라즈베리 파이 본체와, 게임패드가 네이키드로 그대로 들어나느것이 하드웨어상이나, 사용자가 조작하기에는 불편하다고 생각되어 직접 CAD를 이용하여 본체 케이스를 설계하였습니다.
파일은 github에 업로드하였습니다.

**6. 파일전송을 위한 SAMBA**

![화면 캡처 2024-12-03 224917](https://github.com/user-attachments/assets/c4f125cf-08c7-4f36-934f-91f615c0091b)

이미 usb 케이블과 VScode를 이용한 원격 개발환경을 마련했으나, 게임상에 필요한 애니메이션이나, 이미지, 화면등을 구현하기위해서는 메인 컴퓨터와 라즈베리파일간의 원활한 파일송신이 필요했습니다. 그래서 저는  SAMBA 패키지를 설치하여, 윈도우 파일탐색기에서 감지되는 공유폴더를 라즈베리파이에 구축하였습니다. 이를 통해 쉽게 라즈베리파이로 파일을 송수신 할수 있었습니다.


## 문제점과 해결책

게임을 개발하면서 발생했던 문제점과 이에 대한 해결책들은 아래와 같습니다.

**1. 충돌 검사 및 상태 업데이트 관련 문제**

- 발생한 문제

여러 클래스(특히 Bullet과 Enemy)에서 충돌 검사를 처리하면서 상태 변경이 제대로 이루어지지 않는 경우가 자주 있었습니다.
예를 들어, 총알이 적군과 충돌했을 때 적군의 상태를 'die'로 변경하고, 총알 상태를 'exploding'으로 변경하는 작업이 있었는데, 
충돌이 제대로 감지되지 않거나 상태가 갱신되지 않는 경우가 발생하여, 어느 if 문에서 발생한 문제인지,
아니면 좌표점 업데이트가 잘못된것인지 확인하느라 많은 시간을 사용하였습니다.

- 사용한 해결법

Python 창에서 로그를 띄우도록해 충돌 검사 로직을 점검하고, 각 객체들의 state가 올바르게 변경되었는지 일일히 검토하며 진행하였습니다.

**2. 게임 내 중력구현 문제**

- 발생한 문제 

물리적인 상호작용(예: 중력, 총알의 궤적, 충돌 등)에 대한 처리가 일관되지 않거나 부족한 부분이 있었습니다.
제일 힘들었던 작업중 하나는, 총알이 발사된 후 중력에 의해 궤적이 변경되도록 하였는데, 처음에는 x, y 값이 일정하게 감소하게 짰으나 이는 그냥 대각선으로 총알이 떨어지는 결과물을 보여주는 문제가 일어났습니다.

- 사용한 해결법

검색포털에서 많은 자료들과 예제들을 확인하면서 최적의 계산공식을 찾을수있었습니다.

**3. 게임 오브젝트의 위치 및 크기 계산 문제**

- 발생한 문제

Bullet 클래스나 Enemy 클래스에서 위치와 크기를 계산하는 방식이 초기 코드에서는 불완전하여 오류가 발생하여 코드가 아예 종료되는 경우나, 아니면 총알이 랜더된 오브젝트를 무시하고 지나가는 경우가 있었습니다. 예를 들어, 캐릭터가 발사한 총알이 적군이 랜더된 곳을 지나가는데 충돌판정 위치는 아예 다른곳에 있어서 그냥 총알이 무시하고 지나가는 경우가 있었습니다.

- 사용한 해결법

1번에서 사용하였던 방식을 채용했습니다. 직접 python 창에 로그를 띄우도록해서 오브젝트의 범위를 정확히 알아낸 뒤, 코드를 수정해 해결했습니다.

**4. 게임 내 상태 변경 및 애니메이션 문제**

- 발생한 문제

객체들의 상태 변경(예: 'active', 'exploding', 'finished')과 애니메이션 처리에 있어, 상태가 변경되었을 때 애니메이션이나 다른 효과가 제대로 반영되지 않는 경우가 있었습니다.
예를 들어, 총알이 폭발 상태로 변경되었을 때 폭발 애니메이션이 적절하게 진행되지 않거나, 애니메이션이 끝난 후 상태가 finished로 갱신되지 않는 경우가 발생해, 폭발 애니메이션의 마지막 프레임의 잔상이 캐릭터나, 지형, 적군에 남는 문제가있었습니다..

- 사용한 해결법

애니메이션 상태를 animate_explosion 메서드에서 관리하고, 애니메이션이 끝난 후 state를 'finished'로 정확히 변경하는지 시스템 로그를 통해 확인해 해결했습니다.

**5. 입력 처리 및 조이스틱 관련 문제**

- 발생한 문제

joystick.py에서 사용자 입력을 처리할 때, 지형에서 허용한 범위값을 넘어가면 인터럽트가 발생하면서 아예 게임이 멈추는 문제가 있었습니다.

- 사용한 해결법

좌표값을 조절해가며 최적의 값을 찾았습니다.

**6. 게임 오브젝트의 렌더링 문제**

- 발생한 문제

여러 게임 객체를 화면에 렌더링할 때, 화면이 제대로 업데이트되지 않거나, 객체들이 올바르게 배치되지 않는 문제가 발생했습니다.
발생했던 문제로는, 배경 이미지와 캐릭터, 적군 등이 서로 겹쳐서 보이는 경우나, 렌더링 순서가 잘못되어 화면에 일부 오브젝트가 보이지 않거나, 애니메이션의 잔상이 캐릭터나 적군에게 남아있거나, 아예 화면이 뜨지않는 문제가 발생하는 등의 문제가 발생하였습니다.

- 사용한 해결법

화면이 올바르게 출력될때의 게임의 각 오브젝트의 렌더링 순서를 문서화 한 뒤, 그 이후로는 문제가 발생하지않았습니다.




## 코드설명

각 코드에 대한 세분화된 설명은 게임 디렉토리 안 각 py 파일에 주석처리 되어있습니다.
아래 내용들은 각 py의 큰 역할에 대한 설명을 작성하였습니다.

**1. enemy.py** 

- 코드 역할

게임에서 적군을 나타내는 클래스입니다.

- 주요 기능

적군 생성: 적군의 위치, 크기, 이미지 등을 초기화합니다.

위치 업데이트: 적군이 일정 거리만큼 x축으로 이동할 수 있도록 update_position 메서드로 위치를 업데이트합니다.

중앙 좌표 계산: 적군의 위치에서 중심 좌표를 계산할 수 있는 get_center 메서드를 제공합니다.

상태 관리: 적군의 상태 ('alive', 'die')를 관리합니다.

실행 예시: 적군이 게임 화면을 가로지르며 이동하고, 충돌할 경우 적군의 상태를 'die'로 변경하는데 사용됩니다.


**2. bullet.py (총알 클래스)**

- 코드 역할

게임에서 총알을 관리하는 클래스입니다.

- 주요 기능

총알 생성 및 초기화: 총알의 초기 위치, 속도, 각도, 이미지, 폭발 애니메이션 등을 초기화합니다.

이동: 총알이 일정 시간 간격으로 이동하도록 move 메서드를 제공합니다. 중력과 속도를 고려하여 총알의 위치를 업데이트합니다.

충돌 처리: collision_check 메서드로 다른 객체(주로 적군이나 캐릭터)와 충돌하는지 확인하고, 충돌 시 적군을 죽이거나 체력을 감소시킵니다.

지형 충돌: terrain_collision_check 메서드로 지형과의 충돌을 처리합니다.

폭발 애니메이션: 충돌 시 폭발 애니메이션을 진행하는 animate_explosion 메서드를 제공합니다.

중앙 좌표 계산: 총알의 중심을 계산하여 반환하는 get_center 메서드가 있습니다.

실행 예시: 총알이 발사된 후 이동하며, 적군과 충돌 시 적군을 죽이고 폭발 애니메이션을 실행합니다.


**3. main.py (게임 실행 및 메인 루프)**

- 코드 역할

게임의 메인 루프와 게임 흐름을 제어, 및 화면에 게임을 랜더링 하는 파일입니다.

- 주요 기능

게임 화면 업데이트: main() 함수에서 주기적으로 화면을 업데이트하며, 캐릭터, 적군, 총알, 지형 등 게임의 모든 요소를 렌더링합니다.

캐릭터 및 총알 발사: 캐릭터의 상태 및 위치를 업데이트하고, 사용자 입력(조이스틱, 버튼)에 따라 총알을 발사합니다.

적군 총알: 적군이 일정 시간 간격으로 총알을 발사하는 기능을 구현합니다.

충돌 처리: 총알과 적군, 총알과 지형, 총알과 캐릭터 간의 충돌을 처리합니다.

애니메이션 및 상태 업데이트: 캐릭터의 이동 애니메이션과 폭발 애니메이션을 처리합니다.

게임 UI: 체력 바와 같은 게임 UI 요소를 화면에 그립니다.

실행 예시: main.py는 게임의 메인 루프를 실행하여 게임을 지속적으로 업데이트하고, 모든 객체의 상태를 갱신하고 화면을 업데이트 합니다.

**4. character.py (캐릭터 클래스)**

- 코드 역할

게임 캐릭터의 동작과 속성을 관리하는 클래스입니다.

- 주요 기능

캐릭터 상태: 캐릭터의 위치, 크기, 이미지 등을 설정합니다.

애니메이션 처리: 캐릭터가 이동할 때 애니메이션을 처리하여, 걷기/멈추기와 같은 동작을 이미지로 표현합니다.

체력 관리: 캐릭터가 총알에 맞을 때 체력을 관리하고, 체력이 0이 되면 죽는 처리를 합니다.

실행 예시: main.py에서 캐릭터의 상태와 위치를 업데이트하며, 키 입력이나 버튼 입력에 따라 캐릭터의 애니메이션 및 이동을 처리합니다.


**5. joystick.py (조이스틱 클래스)**

- 역할

조이스틱 입력을 관리하는 클래스입니다.

- 주요 기능

입력 처리: 사용자로부터의 조이스틱 입력(버튼, 방향)을 처리하여 캐릭터의 움직임을 제어합니다.

디스플레이: 게임 화면을 출력하는 기능도 포함되어 있습니다. 디스플레이는 화면을 갱신하고, 그 위에 캐릭터, 총알, 적군, 지형 등을 그립니다.

실행 예시: main.py에서 조이스틱 입력에 따라 캐릭터 이동 및 총알 발사 등을 처리합니다.
