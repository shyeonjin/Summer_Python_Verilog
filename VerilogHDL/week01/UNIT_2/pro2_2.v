// 4-비트 리플 케리 카운터

// top-down 설계 방법: 
// 먼저 최상의 블록인 리플 캐리 카운터의 기능들을 정의하고, T_FF를 가지고 카운터를 구현한다.
// T_FF는 D_FF와 인버터를 가지고 구현할 수 있다.
// 그러므로, 큰 블록을 더 이상 나누어지지 않는 하위블록까지 나눌 수 있다.

// bottom-up 설계 방법: top_down 설계 방법과 반대의 흐름을 가진다.
// 작은 블록들을 조합해서 더 큰 블록들을 만든다.
// 예를 들어 D_FF를 and나 or게이트를 사용해서 만들거나, 트랜지스터를 이용해서 만들 수 있다.
// 그러므로 bottom-up 방법의 흐름과 top-down 방법의 흐름이 D_FF의 단계에서 만나게 된다. 