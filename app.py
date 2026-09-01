import random
import streamlit as st

# ページの基本設定
st.set_page_config(
    page_title="10日観光案内", page_icon="🗺️", layout="centered"
)

# --- ホラー風フォント用のカスタムCSS ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Creepster&family=Mochiy+Pop+One&display=swap');

    .horror-text {
        font-family: 'Creepster', cursive, sans-serif;
        color: #ff0033;
        font-size: 1.1rem;
        letter-spacing: 1px;
        line-height: 1.6;
    }
    .date-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #ff4b4b;
        margin-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- 架空の人気観光地10種データ（テキストを長めに修正） ---
ALL_SPOTS = [
    {
        "id": "spot_1",
        "name": "セレスティア浮遊島",
        "normal_text": "雲の遥か上空に悠然と浮かぶ神聖なる天空の島。中心にそびえ立つ大聖堂からは、毎日定刻になると澄み切った黄金の鐘の音が響き渡り、訪れるすべての旅人の心を深く癒やしてくれます。島内には色鮮やかな天空の花々が咲き乱れ、穏やかな風が吹き抜ける楽園として多くの観光客に愛され続けています。",
        "normal_image": "images/selestia.jpg",
        "horror_image": "images/negaselestia.jpg",
        "fake_name": "墜落せるセレスティア廃墟",
        "horror_text": "雲の遥か上空に浮かぶはずの島は見る影もなく崩壊している。黄金の鐘の音は完全に止み、代わりに参加者たちの絶叫と血の雨が人々の精神を狂わせる。血塗られた鐘の残骸だけが、訪れた者に終わりのない絶望と逃れられない狂気を告げ続けている。",
    },
    {
        "id": "spot_2",
        "name": "ネオンヴェール水晶宮",
        "normal_text": "七色にまばゆく輝く巨大なクリスタルで全体が構築された、息をのむほど幻想的な宮殿。ドーム型の天井からは星屑のような光が降り注ぎ、宮殿の専属楽団による心地よい弦楽器の調べが館内を優しく包み込みます。夜になるとクリスタルがライトアップされ、言葉を失うほどの美しさを堪能できます。",
        "normal_image": "images/neon.jpg",
        "horror_image": "images/neganeon.jpg",
        "fake_name": "呪縛のネオンヴェール牢獄",
        "horror_text": "七色に輝くはずのクリスタルはどす黒く濁り、不気味な脈動を繰り返している。かつての美しい弦楽の調べは耳をつんざくような悲鳴へと変わり、透明な水晶の壁の内部には、閉じ込められた無数の歪んだ人間の顔が無数に浮かび上がりながらこちらを睨みつけている。",
    },
    {
        "id": "spot_3",
        "name": "アストラル星見台",
        "normal_text": "遮るものが何もない高台にそびえ立つ、世界最大級の巨大な天体観測施設。夜空に広がる満天の星々や天の川を肉眼でも鮮明に捉えることができ、天文ファンにとっては聖地とも言える場所です。備え付けの大型望遠鏡を覗けば、時空を超えた宇宙の神秘を肌で感じ、心地よい夜風が火照った頬をクールダウンしてくれます。",
        "normal_image": "images/astral.jpg",
        "horror_image": "images/negaastrai.jpg",
        "fake_name": "アストラル死霊観測所",
        "horror_text": "頭上に広がっていたはずの満天の星空は完全に消え去り、漆黒の虚無が広がっている。巨大な望遠鏡のレンズを覗き込んではならない。そこには地球のものではない巨大な眼球が、暗闇の中からあなたをロックオンして這い寄ってくる恐ろしい光景が映し出されている。",
    },
    {
        "id": "spot_4",
        "name": "ヴェルデ深緑の迷宮庭園",
        "normal_text": "何世代にもわたって手入れされてきた、どこまでも続く美しく巨大な緑の生垣迷路。高さ3メートルを超える幾何学的な植え込みを抜けながら、ゴールを目指す爽快なアクティビティとしてファミリー層に大人気です。足元には可愛らしい小鳥たちがさえずり、緑豊かなアロマの香りが日々の疲れをリフレッシュさせます。",
        "normal_image": "images/verude.jpg",
        "horror_image": "images/negaverude.jpg",
        "fake_name": "ヴェルデ血塗られた茨の庭",
        "horror_text": "美しかった緑の生垣は鋭い黒い茨へと変貌し、歩くたびに衣服を引き裂く。可愛らしい小鳥のさえずりは、迷路のあちこちに転がる無残な死体の群れから発せられる呻き声へと変わった。一度足を踏み入れたが最後、出口にたどり着く者は二度と生きて帰ることはできない。",
    },
    {
        "id": "spot_5",
        "name": "オーロラ・グレイシャー",
        "normal_text": "太陽光を受けて青白く神々しく輝く、壮大で圧倒的なスケールの巨大氷河。一年を通して澄んだ冷涼な空気に満たされており、夜間には頭上に鮮やかなエメラルドグリーンのオーロラが優雅に揺らめきます。氷の洞窟ツアーでは、数万年の時を閉じ込めた神秘的なブルーの氷の世界を安全に体験できます。",
        "normal_image": "images/orora.jpg",
        "horror_image": "images/negaorora.jpg",
        "fake_name": "凍結せる呪いの氷壁",
        "horror_text": "青白く輝いていたはずの氷河は赤黒く凍てつき、周囲の空気は息が凍るほどの殺気で満ちている。オーロラではなく不気味な紫色の歪んだ光が揺らめく中、分厚い氷の壁の内側から、凍えながらも助けを求めて必死に引っ掻き傷をつける無数の冷たい手がこちらに伸びている。",
    },
    {
        "id": "spot_6",
        "name": "サンセット・ミラージュ港",
        "normal_text": "水平線に沈む夕陽が海面をどこまでも鮮やかな黄金色に染め上げる、穏やかで美しい港町。毎夕開催される名物の朝市（夕市）では、地元の漁師たちが獲れたての新鮮な海の幸を豪快に振る舞い、観光客と地元住民の笑顔と活気ある賑わいに包まれています。潮風が心地よい最高のロケーションです。",
        "normal_image": "images/sun.jpg",
        "horror_image": "images/negasun.jpg",
        "fake_name": "難破船の墓場サンセット港",
        "horror_text": "夕陽で黄金色に染まるはずの海面は血の海のようにドロドロに濁り、異臭を放っている。活気あるはずの市場の屋台には、魚介類の代わりに腐敗した生肉と、生々しい人間の眼球や臓器が生々しくずらりと並べられている。誰もいない桟橋から、海面に向かって引きずり込まれる足音が近づく。",
    },
    {
        "id": "spot_7",
        "name": "クロノス古代時計塔",
        "normal_text": "中世の建築美をそのまま残し、遥かなる時を正確に刻み続ける荘厳な大時計塔。歴史のロマンを感じさせる巨大な歯車が組み合わさり、毎正時になると街中に心地よい美しいメロディが流れて人々を魅了します。塔の展望台からは街全体が一望でき、写真撮影のスポットとしても絶大な人気を誇っています。",
        "normal_image": "images/clonos.jpg",
        "horror_image": "images/negaclonos.jpg",
        "fake_name": "時を止める断頭時計塔",
        "horror_text": "時を刻むはずの巨大な針は恐ろしい速度で逆回転を始め、塔全体が耳障りな金切り声を上げている。毎正時に流れるはずのメロディは、処刑台のギロチンが落下する不気味な金属音に置き換わり、時計の歯車の間からは無数の血飛沫が絶えず滴り落ちている。",
    },
    {
        "id": "spot_8",
        "name": "シルフィード風車村",
        "normal_text": "見渡す限りのなだらかな緑の丘陵に、白い巨大な風車がゆっくりと並び立つ牧歌的な村。常に心地よいそよ風が吹き抜けており、伝統的な牧畜文化が息づくのどかな風景が広がっています。村の工房で焼き上げられる香ばしい自家製パンと新鮮なミルクは、旅の疲れを優しく癒やしてくれる最高の贅沢です。",
        "normal_image": "images/silfu.jpg",
        "horror_image": "images/negasilf.jpg",
        "fake_name": "狂気の風車挽肉村",
        "horror_text": "のどかな丘に並ぶ巨大な風車の羽は猛烈な勢いで回転し、周囲に異常な風圧を撒き散らしている。風車の内部から聞こえてくるのは風の音ではなく、巨大な石臼ですり潰される人間の骨が激しく砕ける、おぞましい轟音と叫び声である。",
    },
    {
        "id": "spot_9",
        "name": "ルミナス黄金神殿",
        "normal_text": "古代の太陽神を祀る、太陽の光を浴びてまばゆく黄金色に輝く神聖な大神殿。精巧な彫刻が施された巨大な柱が立ち並び、神殿の内部では世界の平和と豊穣を祈る厳かな儀式が日々執り行われています。神殿の周囲に広がる聖なる泉の水面は鏡のように空を映し出し、訪れる者に神秘的な安らぎをもたらします。",
        "normal_image": "images/ruminas.jpg",
        "horror_image": "images/negaruminas.jpg",
        "fake_name": "冒涜の生贄神殿",
        "horror_text": "太陽の光を浴びて輝くはずの黄金はどす黒く錆び果て、神殿全体が禍々しいオーラに包まれている。平和の祈りが捧げられていた祭壇の上には、生贄として捧げられた者たちの肉片が散乱し、神の姿は完全に消え失せ、代わりに得体の知れない肉の塊が蠢いている。",
    },
    {
        "id": "spot_10",
        "name": "アイリス霧の渓谷温泉",
        "normal_text": "深い森と豊かな湯けむりに包まれた、険しい渓谷の奥地にひっそりと佇む秘境の温泉郷。湧き出る天然温泉は神経痛や疲労回復に抜群の効果があると評判で、心身ともに極上のリラクゼーションを味わえます。立ち込める白銀の湯けむりの向こうには、季節ごとに表情を変える美しい渓谷の絶景が広がっています。",
        "normal_image": "images/airis.jpg",
        "horror_image": "images/negaairis.jpg",
        "fake_name": "猛毒の血の池温泉",
        "horror_text": "豊かな湯けむりに包まれているはずの温泉郷一帯は、強烈な酸性の異臭と熱い血煙に覆われている。美しい渓谷の湯船からもうもうと立ち上るのは、沸騰した人間の血と溶解した肉の臭いそのものである。湯に足を踏み入れた瞬間、皮膚がただれて骨へと溶け落ちる。",
    },
]

# --- セッション状態の初期化 ---
if "started" not in st.session_state:
    st.session_state.started = False
if "day" not in st.session_state:
    st.session_state.day = 1
if "current_spots" not in st.session_state:
    st.session_state.current_spots = []
if "has_anomaly" not in st.session_state:
    st.session_state.has_anomaly = False
if "anomaly_type" not in st.session_state:
    st.session_state.anomaly_type = None
if "anomaly_spot_index" not in st.session_state:
    st.session_state.anomaly_spot_index = None
if "message" not in st.session_state:
    st.session_state.message = ""

TOTAL_DAYS = 10


def init_round():
    spots_copy = [dict(s) for s in ALL_SPOTS]

    # 1日目は必ず異変なし（正常）にする
    if st.session_state.day == 1:
        st.session_state.has_anomaly = False
        st.session_state.anomaly_type = None
        st.session_state.anomaly_spot_index = None
    else:
        # 異変の発生率を70%に引き上げ
        st.session_state.has_anomaly = random.choices(
            [True, False], weights=[7, 3], k=1
        )[0]
        st.session_state.anomaly_type = None
        st.session_state.anomaly_spot_index = None

        if st.session_state.has_anomaly:
            anomaly_type = random.choice(
                ["text", "image", "name", "button_reverse", "order_shuffle"]
            )
            st.session_state.anomaly_type = anomaly_type
            target_idx = random.randint(0, len(spots_copy) - 1)
            st.session_state.anomaly_spot_index = target_idx

    # ★変更：ここで一度だけシャッフルを確定させ、セッションに保持する
    if st.session_state.has_anomaly and st.session_state.anomaly_type == "order_shuffle":
        random.shuffle(spots_copy)

    st.session_state.current_spots = spots_copy
    st.session_state.message = ""


# --- ゲーム画面の構築 ---
st.title("🗺️ 10日観光案内")

# スタート画面
if not st.session_state.started:
    st.markdown("---")
    st.subheader("【ルール説明】")
    st.markdown(
        """
    * 8/10から8/19までの10日間、架空の10大観光地ガイドをチェックしながら脱出を目指します。
    * 案内の中にわずかでも**「異変」**がないか、10か所すべてを注意深く観察してください。
    * ※なお、1日目（8/10）は必ず安全な状態（異変なし）から始まります。
    * 発生する異変の種類：
      1. **文章の異変**：特定の案内文がホラー風に変わる
      2. **写真の異変**：特定の写真が不気味なものに変わる
      3. **観光地名の異変**：特定の名称が禍々しいものに変わる
      4. **UIの異変**：アクションボタンの配置が左右逆転する
      5. **配置の異変**：観光地の並び順がいつもと違っている
    * **異変がある場合**：**「🔄 再読み込みする」** ボタンを押す。
    * **異変がない場合**：**「➡️ 次の観光案内へ（1日進む）」** ボタンを押す。
    * 間違うと、容赦なく **1日目（8/10）** に戻されます。
    """
    )
    if st.button("ゲームスタート", type="primary", use_container_width=True):
        st.session_state.started = True
        st.session_state.day = 1
        init_round()
        st.rerun()

# クリア画面（8/20表示）
elif st.session_state.day > TOTAL_DAYS:
    st.markdown("---")
    st.markdown(
        '<div class="date-header">📅 8月20日（クリア・脱出成功）</div>',
        unsafe_allow_html=True,
    )
    st.success(
        "🎉 おめでとうございます！10日間のすべての異変を完璧に見抜き、8月20日を迎えて無事に現実世界へ脱出成功しました！"
    )
    st.balloons()
    if st.button("もう一度プレイする", use_container_width=True):
        st.session_state.started = False
        st.session_state.day = 1
        st.rerun()

# プレイ中画面（8/10 ~ 8/19）
else:
    current_date_str = f"8月{9 + st.session_state.day}日"

    st.markdown(
        f'<div class="date-header">📅 {current_date_str} (第 {st.session_state.day} 日目 / 全 {TOTAL_DAYS} 日)</div>',
        unsafe_allow_html=True,
    )
    st.progress(st.session_state.day / TOTAL_DAYS)
    st.markdown("---")

    spots = st.session_state.current_spots
    is_button_reversed = False

    
    # UI異変チェック
    if (
        st.session_state.has_anomaly
        and st.session_state.anomaly_type == "button_reverse"
    ):
        is_button_reversed = True

    # 10種の観光案内を2つずつ並べて表示するために、2つずつのペアに分割
    for i in range(0, len(spots), 2):
        col_pair1, col_pair2 = st.columns(2)

        # 1つ目のスポット
        spot1 = spots[i]
        idx1 = ALL_SPOTS.index(
            next(s for s in ALL_SPOTS if s["id"] == spot1["id"])
        )  # 元のインデックスではなく現在の表示順位置
        # 表示中のリスト内でのインデックス
        actual_idx1 = i

        display_name1 = spot1["name"]
        display_text1 = spot1["normal_text"]
        display_image1 = spot1["normal_image"]
        is_text_anomaly1 = False

        if (
            st.session_state.has_anomaly
            and st.session_state.anomaly_spot_index is not None
        ):
            # どのスポットに異変が仕込まれているかをIDベースで判定できるようにする
            pass

    # スポットごとの描画を綺麗に行うため、リストを直接ループして2カラムに分けるより、
    # 2つずつペアを作る形ですべてのカードを生成する
    for i in range(0, len(spots), 2):
        cols = st.columns(2)

        # 左側のスポット
        with cols[0]:
            spot_a = spots[i]
            # ALL_SPOTS または元のリストにおけるこのスポットの元の位置を特定、あるいは現在のインデックスを使う
            # ここではシンプルに、現在の spots リスト上のインデックス i をターゲットと比較する
            idx_a = i
            name_a = spot_a["name"]
            text_a = spot_a["normal_text"]
            image_a = spot_a["normal_image"]
            is_anomaly_text_a = False

            if (
                st.session_state.has_anomaly
                and st.session_state.anomaly_spot_index == idx_a
            ):
                atype = st.session_state.anomaly_type
                if atype == "text":
                    text_a = spot_a["horror_text"]
                    is_anomaly_text_a = True
                elif atype == "image":
                    image_a = spot_a["horror_image"]
                elif atype == "name":
                    name_a = spot_a["fake_name"]

            with st.container(border=True):
                st.markdown(f"### 📍 [{idx_a+1}/10] {name_a}")
                st.image(image_a, use_container_width=True, caption="公式ガイド")
                if is_anomaly_text_a:
                    st.markdown(
                        f'<p class="horror-text">{text_a}</p>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.write(text_a)

        # 右側のスポット（存在する場合）
        if i + 1 < len(spots):
            with cols[1]:
                spot_b = spots[i + 1]
                idx_b = i + 1
                name_b = spot_b["name"]
                text_b = spot_b["normal_text"]
                image_b = spot_b["normal_image"]
                is_anomaly_text_b = False

                if (
                    st.session_state.has_anomaly
                    and st.session_state.anomaly_spot_index == idx_b
                ):
                    atype = st.session_state.anomaly_type
                    if atype == "text":
                        text_b = spot_b["horror_text"]
                        is_anomaly_text_b = True
                    elif atype == "image":
                        image_b = spot_b["horror_image"]
                    elif atype == "name":
                        name_b = spot_b["fake_name"]

                with st.container(border=True):
                    st.markdown(f"### 📍 [{idx_b+1}/10] {name_b}")
                    st.image(
                        image_b, use_container_width=True, caption="公式ガイド"
                    )
                    if is_anomaly_text_b:
                        st.markdown(
                            f'<p class="horror-text">{text_b}</p>',
                            unsafe_allow_html=True,
                        )
                    else:
                        st.write(text_b)

    if is_button_reversed:
        st.caption("（※ボタンの並び順に妙な違和感がある……）")

    if st.session_state.message:
        st.warning(st.session_state.message)

    st.markdown("### 🎛️ アクション選択")

    col1, col2 = st.columns(2)


    def handle_choice(chose_reload: bool):
        if chose_reload == st.session_state.has_anomaly:
            st.session_state.day += 1
            init_round()
            st.rerun()
        else:
            st.session_state.day = 1
            init_round()
            if st.session_state.has_anomaly:
                st.session_state.message = (
                    "❌ 異変を見落とした！8月10日（1日目）に戻されます。"
                )
            else:
                st.session_state.message = (
                    "❌ 異変はないのに再読み込みしてしまった！8月10日（1日目）に戻されます。"
                )
            st.rerun()


    if not is_button_reversed:
        with col1:
            if st.button(
                "➡️ 次の観光案内へ\n(異変なし)",
                key="btn_next_normal",
                use_container_width=True,
                type="secondary",
            ):
                handle_choice(chose_reload=False)
        with col2:
            if st.button(
                "🔄 再読み込みする\n(異変あり)",
                key="btn_reload_normal",
                use_container_width=True,
                type="primary",
            ):
                handle_choice(chose_reload=True)
    else:
        with col1:
            if st.button(
                "🔄 再読み込みする\n(異変あり)",
                key="btn_reload_rev",
                use_container_width=True,
                type="primary",
            ):
                handle_choice(chose_reload=True)
        with col2:
            if st.button(
                "➡️ 次の観光案内へ\n(異変なし)",
                key="btn_next_rev",
                use_container_width=True,
                type="secondary",
            ):
                handle_choice(chose_reload=False)
