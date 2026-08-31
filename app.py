import random
import streamlit as st

# ページの基本設定
st.set_page_config(
    page_title="異変観光案内からの脱出", page_icon="🗺️", layout="centered"
)

# --- 定数・観光地データ ---
# 観光地ごとの通常状態（正常）のテキストと画像（プレースホルダー）
SPOTS = [
    {
        "name": "フランス・パリ（エッフェル塔）",
        "normal_text": "快晴のパリ。エッフェル塔が美しくそびえ立っています。鳥が優雅に飛んでいます。",
        "normal_image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "アメリカ・ニューヨーク（自由の女神）",
        "normal_text": "青空の下、ニューヨーク港にたたずむ自由の女神。海面も穏やかです。",
        "normal_image": "https://images.unsplash.com/photo-1485738422979-f5c462d49f74?auto=format&fit=crop&w=800&q=80",
    },
    {
        "name": "イタリア・ローマ（コロッセオ）",
        "normal_text": "歴史あるコロッセオ。周囲の空は明るく、観光客でにぎわっています。",
        "normal_image": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=800&q=80",
    },
]

# 異変のバリエーション（テキストや画像の変更・不気味な要素）
ANOMALIES = [
    {
        "type": "text",
        "desc": "【異変】案内文の一部が不気味に書き換わっている……！",
        "modifier": lambda t: t.replace("美しい", "血のように赤い").replace(
            "穏やか", "荒れ狂う"
        )
        + " ……ここから逃げろ。",
    },
    {
        "type": "image",
        "desc": "【異変】空の色や景色の様子がどこかおかしい……！",
        "modifier_img": lambda img: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=800&q=80",  # 不気味な色合いの写真などに差し替え
    },
]

# --- セッション状態の初期化 ---
if "started" not in st.session_state:
    st.session_state.started = False
if "stage" not in st.session_state:
    st.session_state.stage = 0  # 0〜MAX_STAGE で脱出
if "current_spot" not in st.session_state:
    st.session_state.current_spot = None
if "has_anomaly" not in st.session_state:
    st.session_state.has_anomaly = False
if "anomaly_data" not in st.session_state:
    st.session_state.anomaly_data = None
if "message" not in st.session_state:
    st.session_state.message = ""

MAX_STAGE = 5  # 5回正解でクリア


def init_round():
    """新しいステージ（観光案内）の状態をランダムに生成する"""
    st.session_state.current_spot = random.choice(SPOTS)
    # 50%の確率で異変を発生させる
    st.session_state.has_anomaly = random.choice([True, False])

    if st.session_state.has_anomaly:
        st.session_state.anomaly_data = random.choice(ANOMALIES)
    else:
        st.session_state.anomaly_data = None
    st.session_state.message = ""


# --- ゲーム画面の構築 ---
st.title("🗺️ 異変観光案内からの脱出")
st.markdown("---")

# スタート画面
if not st.session_state.started:
    st.subheader("【ルール説明】")
    st.markdown(
        """
    * 世界各地の観光案内ページを次々とチェックしていきます。
    * 案内の中に**「異変」**（文章や写真の違和感）がないか注意深く観察してください。
    * **異変がある場合**：**「🔄 再読み込みする」**ボタンを押してください。
    * **異変がない場合**：**「➡️ 次の観光案内へ」**ボタンを押してください。
    * 選択を間違えると、**振り出しに戻されます**。
    * 全 **5ステージ** を突破して無事に現実世界へ帰りましょう！
    """
    )
    if st.button("ゲームスタート", type="primary", use_container_width=True):
        st.session_state.started = True
        st.session_state.stage = 1
        init_round()
        st.rerun()

# クリア画面
elif st.session_state.stage > MAX_STAGE:
    st.success("🎉 おめでとうございます！無事にすべての異変を見抜き、脱出成功です！")
    st.balloons()
    if st.button("もう一度プレイする", use_container_width=True):
        st.session_state.started = False
        st.session_state.stage = 0
        st.rerun()

# プレイ中画面
else:
    # 進捗表示
    st.progress(
        st.session_state.stage / MAX_STAGE,
        text=f"脱出進捗: ステージ {st.session_state.stage} / {MAX_STAGE}",
    )

    spot = st.session_state.current_spot
    display_text = spot["normal_text"]
    display_image = spot["normal_image"]

    # 異変の適用
    if st.session_state.has_anomaly:
        anomaly = st.session_state.anomaly_data
        if anomaly["type"] == "text":
            display_text = anomaly["modifier"](display_text)
        elif anomaly["type"] == "image":
            display_image = anomaly["modifier_img"](display_image)

    # 観光案内風のUIカード
    with st.container(border=True):
        st.markdown(f"### 📍 観光地: {spot['name']}")
        st.image(
            display_image, use_container_width=True, caption=f"公式観光ガイド画像"
        )
        st.write(display_text)

    if st.session_state.message:
        st.warning(st.session_state.message)

    st.markdown("### 🎛️ アクション選択")
    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "➡️ 次の観光案内へ\n(異変なし)",
            use_container_width=True,
            type="secondary",
        ):
            if not st.session_state.has_anomaly:
                # 正解：次のステージへ
                st.session_state.stage += 1
                init_round()
                st.rerun()
            else:
                # 不正解：異変があったのに「異変なし」を選んだ
                st.session_state.stage = 1
                init_round()
                st.session_state.message = (
                    "❌ 残念！異変を見落とした！最初のステージに戻されます。"
                )
                st.rerun()

    with col2:
        if st.button(
            "🔄 再読み込みする\n(異変あり)",
            use_container_width=True,
            type="primary",
        ):
            if st.session_state.has_anomaly:
                # 正解：異変を正しく見抜いてリロードした
                st.session_state.stage += 1
                init_round()
                st.rerun()
            else:
                # 不正解：異変がないのにリロードした
                st.session_state.stage = 1
                init_round()
                st.session_state.message = (
                    "❌ 異変はないのに再読み込みしてしまった！最初のステージに戻されます。"
                )
                st.rerun()
