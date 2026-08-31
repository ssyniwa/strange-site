import random
import streamlit as st

# ページの基本設定
st.set_page_config(
    page_title="異変観光案内からの脱出", page_icon="🗺️", layout="centered"
)

# --- 定数・拡張観光地データ ---
SPOTS = [
    {
        "id": "eiffel",
        "name": "フランス・パリ（エッフェル塔）",
        "normal_text": "快晴のパリ。エッフェル塔が美しくそびえ立っています。鳥が優雅に飛んでいます。",
        "normal_image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=800&q=80",
        "horror_image": "http://googleusercontent.com/image_collection/image_retrieval/11596062876196021433_0",
        "fake_name": "フランス・パリ（絶望の鉄塔）",
    },
    {
        "id": "liberty",
        "name": "アメリカ・ニューヨーク（自由の女神）",
        "normal_text": "青空の下、ニューヨーク港にたたずむ自由の女神。海面も穏やかです。",
        "normal_image": "https://images.unsplash.com/photo-1485738422979-f5c462d49f74?auto=format&fit=crop&w=800&q=80",
        "horror_image": "http://googleusercontent.com/image_collection/image_retrieval/7120418490070298845_0",
        "fake_name": "アメリカ・ニューヨーク（虚無の巨像）",
    },
    {
        "id": "colosseum",
        "name": "イタリア・ローマ（コロッセオ）",
        "normal_text": "歴史あるコロッセオ。周囲の空は明るく、観光客でにぎわっています。",
        "normal_image": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=800&q=80",
        "horror_image": "http://googleusercontent.com/image_collection/image_retrieval/4693885852972669999_0",
        "fake_name": "イタリア・ローマ（血塗られた闘技場）",
    },
    {
        "id": "pyramid",
        "name": "エジプト・ギザ（ピラミッド）",
        "normal_text": "黄金色の砂漠にそびえ立つ雄大なピラミッド。ラクダの隊列が遠くに見えます。",
        "normal_image": "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?auto=format&fit=crop&w=800&q=80",
        "horror_image": "http://googleusercontent.com/image_collection/image_retrieval/8340165340916779065_0",
        "fake_name": "エジプト・ギザ（永遠の墓標）",
    },
    {
        "id": "temple",
        "name": "カンボジア・アンコールワット",
        "normal_text": "緑のジャングルに囲まれた神秘的な遺跡。石壁には精巧なレリーフが刻まれています。",
        "normal_image": "https://images.unsplash.com/photo-1569668297773-8a6f8b9d1469?auto=format&fit=crop&w=800&q=80",
        "horror_image": "http://googleusercontent.com/image_collection/image_retrieval/5977514751489424436_0",
        "fake_name": "カンボジア・アンコールワット（朽ち果てた神殿）",
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

MAX_STAGE = 6  # 6回連続で見抜けばクリア


def init_round():
    """新しいステージの状態をランダムに決定する"""
    st.session_state.current_spot = random.choice(SPOTS)

    # 50%の確率で異変を発生させる
    st.session_state.has_anomaly = random.choice([True, False])

    if st.session_state.has_anomaly:
        # 4種類の異変からランダムに選択
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
    * 世界各地の観光案内ページを次々とチェックし、脱出を目指します。
    * 案内の中に少しでも**「異変」**がないか注意深く観察してください。
    * 異変のバリエーション：
      1. **文章の異変**：不気味な文言への書き換え
      2. **写真の異変**：AIが生成した不気味なホラー風景への変化
      3. **観光地名の異変**：おかしな名称への変化
      4. **UIの異変**：ボタンの配置（左右）の逆転
    * **異変がある場合**：**「🔄 再読み込みする」** ボタンを押す。
    * **異変がない場合**：**「➡️ 次の観光案内へ」** ボタンを押す。
    * 選択を間違えると、**容赦なく最初のステージ（ステージ1）に戻されます**。
    * 全 **6ステージ** を突破して脱出してください！
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

    # 異変の適用
    if st.session_state.has_anomaly:
        atype = st.session_state.anomaly_type
        if atype == "text":
            display_text = (
                "【⚠️警告】この案内文は書き換えられています。「ここから引き返せ」"
            )
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
        st.write(display_text)

        # 異変ヒント（ボタン配置が逆のときだけ、かすかな違和感を視覚的に出す場合など）
        if is_button_reversed:
            st.caption(
                "（※なんだかボタンの並び順に違和感を感じる……？）」"
            )

    if st.session_state.message:
        st.warning(st.session_state.message)

    st.markdown("### 🎛️ アクション選択")

    # ボタン配置（通常 vs 異変による左右逆転）
    col1, col2 = st.columns(2)

    # 判定用の関数
    def handle_choice(chose_reload: bool):
        # chose_reload: True = 「再読み込みする」を選んだ, False = 「次の観光案内へ」を選んだ
        # 実際に異変が存在するかどうか (has_anomalyがTrueならリロードが正解、Falseなら次へが正解)
        if chose_reload == st.session_state.has_anomaly:
            # 正解
            st.session_state.stage += 1
            init_round()
            st.rerun()
        else:
            # 不正解
            st.session_state.stage = 1
            init_round()
            if st.session_state.has_anomaly:
                st.session_state.message = (
                    "❌ 異変があったのに見落とした！最初のステージに戻されます。"
                )
            else:
                st.session_state.message = (
                    "❌ 異変はないのに再読み込みしてしまった！最初のステージに戻されます。"
                )
            st.rerun()


    if not is_button_reversed:
        # 通常の配置: 左が「次の観光案内へ」、右が「再読み込みする」
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
        # UI異変（ボタンの左右逆転）
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
