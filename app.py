import random
import streamlit as st

# ページの基本設定
st.set_page_config(
    page_title="異変観光案内からの脱出", page_icon="🗺️", layout="centered"
)

# --- ホラー風フォント用のカスタムCSS ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Creepster&family=Mochiy+Pop+One&display=swap');

    .horror-text {
        font-family: 'Creepster', cursive, sans-serif;
        color: #ff0033;
        font-size: 1.2rem;
        letter-spacing: 2px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- 架空の人気観光地10種データ ---
SPOTS = [
    {
        "id": "spot_1",
        "name": "セレスティア浮遊島",
        "normal_text": "雲の上に浮かぶ神聖な島。黄金の鐘の音が人々の心を癒やします。",
        "normal_image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
        "horror_image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=800&q=80",
        "fake_name": "墜落せるセレスティア廃墟",
        "horror_text": "雲の上に浮かぶ神聖な島。黄金の鐘の音は止み、血の雨が人々の心を奪う。血塗られた鐘が狂気を告げる。",
    },
    {
        "id": "spot_2",
        "name": "ネオンヴェール水晶宮",
        "normal_text": "七色に輝くクリスタルに囲まれた幻想的な宮殿。美しい音楽が響きます。",
        "normal_image": "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=800&q=80",
        "horror_image": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=800&q=80",
        "fake_name": "呪縛のネオンヴェール牢獄",
        "horror_text": "七色に輝くクリスタルに囲まれた幻想的な宮殿。美しい音楽は絶叫とかわり、クリスタルに無数の顔が浮かぶ。",
    },
    {
        "id": "spot_3",
        "name": "アストラル星見台",
        "normal_text": "満天の星空を観測する巨大な天文台。夜風が心地よく吹き抜けます。",
        "normal_image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
        "horror_image": "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=800&q=80",
        "fake_name": "アストラル死霊観測所",
        "normal_text": "満天の星空を観測する巨大な天文台。星はすべて消え去り、暗闇から何者かが見つめている。",
    },
    {
        "id": "spot_4",
        "name": "ヴェルデ深緑の迷宮庭園",
        "normal_text": "どこまでも続く美しい緑の生垣迷路。可愛らしい小鳥のさえずりが聞こえます。",
        "normal_image": "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=800&q=80",
        "horror_image": "https://images.unsplash.com/photo-1511497584788-876761142212?auto=format&fit=crop&w=800&q=80",
        "fake_name": "ヴェルデ血塗られた茨の庭",
        "normal_text": "どこまでも続く美しい緑の生垣迷路。可愛らしい小鳥のさえずりは死体の群れへと変わる。",
    },
    {
        "id": "spot_5",
        "name": "オーロラ・グレイシャー",
        "normal_text": "青白く輝く巨大な氷河。澄んだ空気の中、オーロラが優雅に揺らめきます。",
        "normal_image": "https://images.unsplash.com/photo-1531366936337-7c912a4589a7?auto=format&fit=crop&w=800&q=80",
        "horror_image": "https://images.unsplash.com/photo-1483921020237-2ff51e8e4b22?auto=format&fit=crop&w=800&q=80",
        "fake_name": "凍結せる呪いの氷壁",
        "normal_text": "青白く輝く巨大な氷河。澄んだ空気の中、氷の中に閉じ込められた者たちが助けを求めている。",
    },
    {
        "id": "spot_6",
        "name": "サンセット・ミラージュ港",
        "normal_text": "夕陽が海面を黄金色に染める穏やかな港町。活気ある市場が人気です。",
        "normal_image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
        "horror_image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=800&q=80",
        "fake_name": "難破船の墓場サンセット港",
        "normal_text": "夕陽が海面を黄金色に染める穏やかな港町。市場には腐敗した生肉と得体の知れない眼球が並ぶ。",
    },
    {
        "id": "spot_7",
        "name": "クロノス古代時計塔",
        "normal_text": "時を刻み続ける荘厳な大時計塔。毎正時に美しいメロディが流れます。",
        "normal_image": "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=800&q=80",
        "horror_image": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=800&q=80",
        "fake_name": "時を止める断頭時計塔",
        "normal_text": "時を刻み続ける荘厳な大時計塔。針は逆回転し、全ての時間は完全に凍てついた。",
    },
    {
        "id": "spot_8",
        "name": "シルフィード風車村",
        "normal_text": "なだらかな丘に並ぶ巨大な風車。のどかな牧歌的風景が広がっています。",
        "normal_image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=800&q=80",
        "horror_image": "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=800&q=80",
        "fake_name": "狂気の風車挽肉村",
        "normal_text": "なだらかな丘に並ぶ巨大な風車。風車の羽から聞こえるのは、何者かの骨が砕ける音だ。",
    },
    {
        "id": "spot_9",
        "name": "ルミナス黄金神殿",
        "normal_text": "太陽の光を浴びてまばゆく輝く神聖な神殿。平和の祈りが捧げられます。",
        "normal_image": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=800&q=80",
        "horror_image": "https://images.unsplash.com/photo-1511497584788-876761142212?auto=format&fit=crop&w=800&q=80",
        "fake_name": "冒涜の生贄神殿",
        "normal_text": "太陽の光を浴びてまばゆく輝く神聖な神殿。黄金はすべて錆び、神の姿は跡形もなく消え失せた。",
    },
    {
        "id": "spot_10",
        "name": "アイリス霧の渓谷温泉",
        "normal_text": "豊かな湯けむりに包まれた秘境の温泉郷。心身をリラックスさせます。",
        "normal_image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
        "horror_image": "https://images.unsplash.com/photo-1483921020237-2ff51e8e4b22?auto=format&fit=crop&w=800&q=80",
        "fake_name": "猛毒の血の池温泉",
        "normal_text": "豊かな湯けむりに包まれた秘境の温泉郷。湯船から立ち上るのは沸騰した血の臭いである。",
    },
]

# --- セッション状態の初期化 ---
if "started" not in st.session_state:
    st.session_state.started = False
if "stage" not in st.session_state:
    st.session_state.stage = 0
if "current_spot" not in st.session_state:
    st.session_state.current_spot = None
if "has_anomaly" not in st.session_state:
    st.session_state.has_anomaly = False
if "anomaly_type" not in st.session_state:
    st.session_state.anomaly_type = None
if "message" not in st.session_state:
    st.session_state.message = ""

MAX_STAGE = 6


def init_round():
    """新しいステージの状態をランダムに決定する"""
    st.session_state.current_spot = random.choice(SPOTS)
    st.session_state.has_anomaly = random.choice([True, False])

    if st.session_state.has_anomaly:
        st.session_state.anomaly_type = random.choice(
            ["text", "image", "name", "button_reverse"]
        )
    else:
        st.session_state.anomaly_type = None

    st.session_state.message = ""


# --- ゲーム画面の構築 ---
st.title("🗺️ 異変観光案内からの脱出")
st.markdown("---")

# スタート画面
if not st.session_state.started:
    st.subheader("【ルール説明 - 8番出口風】")
    st.markdown(
        """
    * 架空の人気観光地ガイドを次々とチェックし、脱出を目指します。
    * 案内の中にわずかでも**「異変」**がないか注意深く観察してください。
    * 異変の種類：
      1. **文章の異変**：ホラー風の不気味な文章への混ざり・変化
      2. **写真の異変**：ホラー風の風景への変化
      3. **観光地名の異変**：禍々しい名称への変化
      4. **UIの異変**：ボタンの配置（左右）の逆転
    * **異変がある場合**：**「🔄 再読み込みする」** ボタンを押す。
    * **異変がない場合**：**「➡️ 次の観光案内へ」** ボタンを押す。
    * 間違うと、**容赦なくステージ1に戻されます**。全6ステージを突破してください！
    """
    )
    if st.button("ゲームスタート", type="primary", use_container_width=True):
        st.session_state.started = True
        st.session_state.stage = 1
        init_round()
        st.rerun()

# クリア画面
elif st.session_state.stage > MAX_STAGE:
    st.success(
        "🎉 おめでとうございます！すべての異変を完璧に見抜き、無事に現実世界へ脱出成功しました！"
    )
    st.balloons()
    if st.button("もう一度プレイする", use_container_width=True):
        st.session_state.started = False
        st.session_state.stage = 0
        st.rerun()

# プレイ中画面
else:
    st.progress(
        st.session_state.stage / MAX_STAGE,
        text=f"脱出進捗: ステージ {st.session_state.stage} / {MAX_STAGE}",
    )

    spot = st.session_state.current_spot

    # 表示用データの初期化（通常）
    display_name = spot["name"]
    display_text = spot["normal_text"]
    display_image = spot["normal_image"]
    is_button_reversed = False
    is_text_anomaly = False

    # 異変の適用
    if st.session_state.has_anomaly:
        atype = st.session_state.anomaly_type
        if atype == "text":
            display_text = spot["horror_text"]
            is_text_anomaly = True
        elif atype == "image":
            display_image = spot["horror_image"]
        elif atype == "name":
            display_name = spot["fake_name"]
        elif atype == "button_reverse":
            is_button_reversed = True

    # 観光案内カードの表示
    with st.container(border=True):
        st.markdown(f"### 📍 観光地: {display_name}")
        st.image(
            display_image, use_container_width=True, caption="公式観光ガイド画像"
        )

        # テキスト異変のときはホラー風フォント/スタイル適用
        if is_text_anomaly:
            st.markdown(
                f'<p class="horror-text">{display_text}</p>',
                unsafe_allow_html=True,
            )
        else:
            st.write(display_text)

        if is_button_reversed:
            st.caption("（※ボタンの並び順に妙な違和感がある……）")

    if st.session_state.message:
        st.warning(st.session_state.message)

    st.markdown("### 🎛️ アクション選択")

    col1, col2 = st.columns(2)


    def handle_choice(chose_reload: bool):
        if chose_reload == st.session_state.has_anomaly:
            st.session_state.stage += 1
            init_round()
            st.rerun()
        else:
            st.session_state.stage = 1
            init_round()
            if st.session_state.has_anomaly:
                st.session_state.message = (
                    "❌ 異変を見落とした！最初のステージに戻されます。"
                )
            else:
                st.session_state.message = (
                    "❌ 異変はないのに再読み込みしてしまった！最初のステージに戻されます。"
                )
            st.rerun()


    if not is_button_reversed:
        with col1:
            if st.button(
                "➡️ 次の観光案内へ\n(異変なし)",
                use_container_width=True,
                type="secondary",
            ):
                handle_choice(chose_reload=False)
        with col2:
            if st.button(
                "🔄 再読み込みする\n(異変あり)",
                use_container_width=True,
                type="primary",
            ):
                handle_choice(chose_reload=True)
    else:
        with col1:
            if st.button(
                "🔄 再読み込みする\n(異変あり)",
                use_container_width=True,
                type="primary",
            ):
                handle_choice(chose_reload=True)
        with col2:
            if st.button(
                "➡️ 次の観光案内へ\n(異変なし)",
                use_container_width=True,
                type="secondary",
            ):
                handle_choice(chose_reload=False)
