import random
import streamlit as st

# =========================================================
# データ定義
# =========================================================
flashcards = [
    # --- 助動詞 + have + PP 一覧 ---
    {
        "word": "must have done",
        "usage": "過去のことへの確信",
        "meaning": "～したに違いない",
        "english_example": "She must have failed the exam.",
        "japanese_example": "彼女は試験に合格しなかったに違いない。"
    },
    {
        "word": "should have done / ought to have done",
        "usage": "過去のことへの推量",
        "meaning": "～したはずだ",
        "english_example": "He should have arrived by now. / He ought to have arrived by now.",
        "japanese_example": "彼は今ごろもう到着したはずだ。"
    },
    {
        "word": "cannot have done",
        "usage": "過去のことへの確信（否定）",
        "meaning": "～したはずがない",
        "english_example": "He cannot have said such a thing.",
        "japanese_example": "彼がそんなことを言ったはずがない。"
    },
    {
        "word": "couldn't have done",
        "usage": "過去のことへの確信（否定）",
        "meaning": "～したはずがない",
        "english_example": "He couldn't have said such a thing.",
        "japanese_example": "彼がそんなことを言ったはずがない。"
    },
    {
        "word": "may have done",
        "usage": "過去のことへの推量",
        "meaning": "～したかもしれない",
        "english_example": "He may have lost his way.",
        "japanese_example": "彼は道に迷ったかもしれない。"
    },
    {
        "word": "might have done",
        "usage": "過去のことへの推量",
        "meaning": "～したかもしれない",
        "english_example": "He might have lost his way.",
        "japanese_example": "彼は道に迷ったかもしれない。"
    },
    {
        "word": "could have done",
        "usage": "過去のことへの推量",
        "meaning": "～したかもしれない",
        "english_example": "He could have lost his way.",
        "japanese_example": "彼は道に迷ったかもしれない。"
    },
    # --- 基本助動詞マスターシート ---
    {
        "word": "can",
        "usage": "能力・可能",
        "meaning": "～することができる",
        "english_example": "She can play the piano.",
        "japanese_example": "彼女はピアノが弾ける。"
    },
    {
        "word": "can",
        "usage": "許可",
        "meaning": "～してもよい",
        "english_example": "You can use my cell phone.",
        "japanese_example": "私の携帯電話を使ってもいいですよ。"
    },
    {
        "word": "can",
        "usage": "依頼",
        "meaning": "～してくれますか",
        "english_example": "Can you open the door?",
        "japanese_example": "ドアを開けてくれますか。"
    },
    {
        "word": "can",
        "usage": "推量（可能性）",
        "meaning": "～はあり得る",
        "english_example": "An accident can happen at any time.",
        "japanese_example": "事故はいつでも起こり得る。"
    },
    {
        "word": "can't",
        "usage": "否定の推量",
        "meaning": "～のはずがない",
        "english_example": "The rumor can't be true.",
        "japanese_example": "そのうわさが本当であるはずがない。"
    },
    {
        "word": "may",
        "usage": "許可",
        "meaning": "～してもよい",
        "english_example": "May I ask you a question?",
        "japanese_example": "質問をしてもよろしいですか。"
    },
    {
        "word": "may",
        "usage": "推量",
        "meaning": "～かもしれない",
        "english_example": "He may be at home.",
        "japanese_example": "彼は家にいるかもしれない。"
    },
    {
        "word": "must",
        "usage": "義務・必要",
        "meaning": "～しなければならない",
        "english_example": "You must get some sleep.",
        "japanese_example": "あなたは少し寝ないといけません。"
    },
    {
        "word": "must",
        "usage": "推量（確信）",
        "meaning": "～に違いない",
        "english_example": "He must be tired.",
        "japanese_example": "彼は疲れているに違いない。"
    },
    {
        "word": "must not",
        "usage": "禁止",
        "meaning": "～してはいけない",
        "english_example": "You must not take pictures here.",
        "japanese_example": "ここで写真を撮ってはいけません。"
    },
    {
        "word": "should (ought to)",
        "usage": "義務・助言",
        "meaning": "～すべきだ",
        "english_example": "You should be more careful.",
        "japanese_example": "君はもっと気を付けるべきだ。"
    },
    {
        "word": "should (ought to)",
        "usage": "推量",
        "meaning": "～のはずだ",
        "english_example": "They should arrive here soon.",
        "japanese_example": "彼らはもうすぐここに着くはずだ。"
    },
    {
        "word": "will",
        "usage": "未来の予測",
        "meaning": "～だろう",
        "english_example": "It will rain this afternoon.",
        "japanese_example": "今日の午後は雨が降るだろう。"
    },
    {
        "word": "will",
        "usage": "意志",
        "meaning": "～するつもりだ",
        "english_example": "I'll do my homework after dinner.",
        "japanese_example": "私は夕食後に宿題をするつもりです。"
    },
    {
        "word": "will / would",
        "usage": "過去の習慣",
        "meaning": "よく～したものだ",
        "english_example": "We would often go to the movies.",
        "japanese_example": "私たちはよく映画を見に行ったものだ。"
    },
    {
        "word": "shall I ～?",
        "usage": "申し出",
        "meaning": "(私が)～しましょうか",
        "english_example": "Shall I open the window?",
        "japanese_example": "窓を開けましょうか。"
    },
    {
        "word": "shall we ～?",
        "usage": "提案",
        "meaning": "(一緒に)～しませんか",
        "english_example": "Shall we go to a movie tomorrow?",
        "japanese_example": "明日、映画に行きませんか。"
    },
    {
        "word": "used to",
        "usage": "過去の習慣",
        "meaning": "(以前は)～したものだ",
        "english_example": "I used to walk to school with my friends.",
        "japanese_example": "私は(以前は)友達と歩いて登校したものだ。"
    },
    {
        "word": "had better",
        "usage": "命令・忠告",
        "meaning": "～しなさい，～するのがよい",
        "english_example": "You had better see a doctor.",
        "japanese_example": "医者に診てもらいなさい。"
    }
]

TOTAL = len(flashcards)

# =========================================================
# ページ設定 & CSS
# =========================================================
st.set_page_config(page_title="助動詞フラッシュカード", layout="centered")

st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: "Yu Gothic", "游ゴシック", "Yu Gothic Medium", "游ゴシック体", sans-serif !important;
        font-size: 26px !important;
        font-weight: 700 !important;
    }

    .stApp {
        background-color: #ffffff;
    }

    h1, h2, h3, .stCaption, p, span, div, label {
        font-family: "Yu Gothic", "游ゴシック", "Yu Gothic Medium", "游ゴシック体", sans-serif !important;
        font-size: 26px !important;
        font-weight: 700 !important;
    }

    h1 {
        color: #4a3f2a !important;
        font-size: 40px !important;
        transform: rotate(-1deg);
    }

    /* --- フラッシュカード本体：手書きノート風 --- */
    .flash-card {
        position: relative;
        border-radius: 10px 14px 12px 16px / 14px 10px 16px 12px;
        padding: 48px 32px;
        min-height: 260px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin-bottom: 28px;
        transform: rotate(-0.6deg);
        box-shadow: 6px 8px 0px rgba(74, 63, 42, 0.15);
    }

    .front-card {
        background: #fffdf6;
        color: #000000;
        border: 3px solid #4a3f2a;
        transform: rotate(0.8deg);
    }

    .back-card {
        background: #fff9e6;
        color: #000000;
        border: 3px solid #b5762c;
        transform: rotate(-0.8deg);
    }

    .card-label {
        font-size: 20px;
        letter-spacing: 3px;
        opacity: 0.6;
        margin-bottom: 10px;
        text-transform: uppercase;
        font-weight: 700;
        border-bottom: 2px dashed #4a3f2a;
        padding-bottom: 6px;
    }

    .card-word {
        font-size: 100px;
        font-weight: 700;
        margin-bottom: 18px;
        line-height: 1.3;
        color: #d32f2f;
        text-decoration: underline;
        text-decoration-style: wavy;
        text-decoration-color: #d32f2f;
        text-underline-offset: 6px;
    }

    .card-usage {
        font-size: 26px;
        font-weight: 700;
        background: #ffe3b3;
        color: #000000;
        display: inline-block;
        padding: 4px 18px;
        border-radius: 999px;
        margin-bottom: 16px;
        border: 2px solid #b5762c;
        transform: rotate(-2deg);
    }

    .card-example {
        font-size: 26px;
        font-weight: 700;
        line-height: 1.7;
        color: #000000;
        opacity: 1;
    }

    .card-meaning {
        font-size: 100px;
        font-weight: 700;
        margin-bottom: 16px;
        color: #000000;
    }

    .stat-box {
        text-align: center;
        border-radius: 12px 16px 14px 18px / 16px 12px 18px 14px;
        padding: 20px 10px;
        font-size: 26px;
        font-weight: 700;
        border: 3px solid #4a3f2a;
        transform: rotate(-1deg);
    }

    /* --- ボタン：手描き風の枠線 --- */
    .stButton > button {
        font-family: "Yu Gothic", "游ゴシック", "Yu Gothic Medium", "游ゴシック体", sans-serif !important;
        font-size: 26px !important;
        font-weight: 700 !important;
        border-radius: 10px 14px 12px 16px / 14px 10px 16px 12px !important;
        border: 3px solid #4a3f2a !important;
        background: #fffdf6 !important;
        color: #2e2a20 !important;
        box-shadow: 3px 4px 0px rgba(74, 63, 42, 0.25);
        transition: transform 0.1s ease-in-out;
    }
    .stButton > button:hover {
        transform: translate(-2px, -2px);
        box-shadow: 5px 6px 0px rgba(74, 63, 42, 0.25);
        color: #b5762c !important;
        border-color: #b5762c !important;
    }
    .stButton > button[kind="primary"] {
        background: #ffe3b3 !important;
        color: #7a4a12 !important;
    }

    /* --- 進捗バー --- */
    .stProgress > div > div {
        background-color: #b5762c !important;
    }

    /* --- チェックボックス・キャプション文字 --- */
    .stCheckbox label, .stCaption, [data-testid="stCaptionContainer"] {
        font-family: "Yu Gothic", "游ゴシック", "Yu Gothic Medium", "游ゴシック体", sans-serif !important;
        font-size: 26px !important;
        font-weight: 700 !important;
        color: #4a3f2a !important;
    }

    /* --- st.metric の数値・ラベル --- */
    [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
        font-family: "Yu Gothic", "游ゴシック", "Yu Gothic Medium", "游ゴシック体", sans-serif !important;
        font-size: 26px !important;
        font-weight: 700 !important;
        color: #4a3f2a !important;
    }
    /* --- サブタイトル文字（小さめ） --- */
    .subtitle-text {
        font-family: "Yu Gothic", "游ゴシック", "Yu Gothic Medium", "游ゴシック体", sans-serif !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        color: #4a3f2a !important;
        opacity: 0.8;
        margin-top: -8px;
        margin-bottom: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# セッション状態の初期化
# =========================================================
def init_session():
    if "started" not in st.session_state:
        st.session_state.started = False
    if "order" not in st.session_state:
        st.session_state.order = list(range(TOTAL))
    if "index" not in st.session_state:
        st.session_state.index = 0
    if "flipped" not in st.session_state:
        st.session_state.flipped = False
    if "good_count" not in st.session_state:
        st.session_state.good_count = 0
    if "review_count" not in st.session_state:
        st.session_state.review_count = 0
    if "review_words" not in st.session_state:
        st.session_state.review_words = []
    if "finished" not in st.session_state:
        st.session_state.finished = False


def reset_all():
    st.session_state.started = False
    st.session_state.order = list(range(TOTAL))
    st.session_state.index = 0
    st.session_state.flipped = False
    st.session_state.good_count = 0
    st.session_state.review_count = 0
    st.session_state.review_words = []
    st.session_state.finished = False


init_session()

st.title("英語 助動詞フラッシュカード")
st.markdown(
    '<p class="subtitle-text">助動詞・助動詞+have+PP の意味と用法をマスターしよう</p>',
    unsafe_allow_html=True,
)

# =========================================================
# スタート画面
# =========================================================
if not st.session_state.started:
    st.write("")
    st.subheader("学習を始めましょう")
    st.write(f"全 **{TOTAL}** 枚のカードが登録されています。")
    shuffle_option = st.checkbox("カードの順番をシャッフルする", value=True)

    if st.button("学習をスタート", type="primary", use_container_width=True):
        order = list(range(TOTAL))
        if shuffle_option:
            random.shuffle(order)
        st.session_state.order = order
        st.session_state.index = 0
        st.session_state.flipped = False
        st.session_state.good_count = 0
        st.session_state.review_count = 0
        st.session_state.review_words = []
        st.session_state.finished = False
        st.session_state.started = True
        st.rerun()

# =========================================================
# 結果画面
# =========================================================
elif st.session_state.finished:
    st.success("全カードを学習しました！お疲れさまでした。")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f"""
            <div class="stat-box" style="background:#eef7e6; color:#3d6b1f; border-color:#6b8f3f;">
                <div style="font-size:36px; font-weight:700;">{st.session_state.good_count}</div>
                <div>覚えた (Good)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"""
            <div class="stat-box" style="background:#fdeee0; color:#a5471f; border-color:#c0602c;">
                <div style="font-size:36px; font-weight:700;">{st.session_state.review_count}</div>
                <div>まだ不安 (Review)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    if st.session_state.review_words:
        st.subheader("復習が必要なカード一覧")
        for item in st.session_state.review_words:
            st.markdown(f"- **{item['word']}** ： {item['meaning']}")
    else:
        st.info("復習が必要なカードはありません。素晴らしい！")

    st.write("")
    if st.button("最初からやり直す", type="primary", use_container_width=True):
        reset_all()
        st.rerun()

# =========================================================
# 学習画面
# =========================================================
else:
    current_idx = st.session_state.order[st.session_state.index]
    card = flashcards[current_idx]

    # 進捗バー
    progress_num = st.session_state.index + 1
    st.progress(progress_num / TOTAL)
    st.caption(f"{progress_num} / {TOTAL} 問目")

    st.write("")

    # カード表示
    if not st.session_state.flipped:
        st.markdown(
            f"""
            <div class="flash-card front-card">
                <div class="card-label">Question</div>
                <div class="card-word">{card['word']}</div>
                <div class="card-example">{card['english_example']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="flash-card back-card">
                <div class="card-label">Answer</div>
                <div class="card-usage">{card['usage']}</div>
                <div class="card-meaning">{card['meaning']}</div>
                <div class="card-example">{card['japanese_example']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # コントロールボタン
    if not st.session_state.flipped:
        if st.button("カードをめくる（裏返す）", type="primary", use_container_width=True):
            st.session_state.flipped = True
            st.rerun()
    else:
        st.write("この助動詞の意味、覚えていましたか？")
        col_good, col_review = st.columns(2)

        def go_to_next(is_good):
            if is_good:
                st.session_state.good_count += 1
            else:
                st.session_state.review_count += 1
                st.session_state.review_words.append(card)

            st.session_state.index += 1
            st.session_state.flipped = False

            if st.session_state.index >= TOTAL:
                st.session_state.finished = True

        with col_good:
            if st.button("覚えた (Good)", use_container_width=True):
                go_to_next(True)
                st.rerun()
        with col_review:
            if st.button("まだ不安 (Review)", use_container_width=True):
                go_to_next(False)
                st.rerun()

    st.write("")
    st.divider()
    stat_col1, stat_col2 = st.columns(2)
    stat_col1.metric("覚えた", st.session_state.good_count)
    stat_col2.metric("まだ不安", st.session_state.review_count)

    st.write("")
    if st.button("終了する", use_container_width=True):
        reset_all()
        st.rerun()