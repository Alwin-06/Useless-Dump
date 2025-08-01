import streamlit as st

st.set_page_config(page_title="Oru Naadan Proposal Success Meter 💘", page_icon="💘")

st.title("💘 Oru Naadan Proposal Success Meter")
st.write("*Enter your name and your crush's name to see your love success chance (naadan version).*")

# Input fields
your_name = st.text_input("Your Name:")
crush_name = st.text_input("Crush's Name:")

def flames_result(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    # Remove common characters
    for char in name1[:]:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    total = len(name1 + name2)

    flames = ["F", "L", "A", "M", "E", "S"]
    while len(flames) > 1:
        split_index = total % len(flames) - 1
        if split_index >= 0:
            flames = flames[split_index+1:] + flames[:split_index]
        else:
            flames = flames[:-1]
    return flames[0]

# Naadan commentary for each FLAMES result
naadan_flames = {
    "F": "😎 *Just friends, alle... Chaya kudikkumbol parayanam, 'just friend aanu'*",
    "L": "🔥 *Love undu. Go propose with bajji and nannari sharbat!*",
    "A": "🥰 *Affection aanu... pinne ninte kaiyil aanu sagalam. Treat chytholum!*",
    "M": "💍 *Kalyanam direct cheytholu! Booking Kalyana mandapam now!*",
    "E": "😤 *Enemy aakum. Ninte reethiyil paranjaal – 'ente mone Dineshaa!' Avoid cheyyu.*",
    "S": "🙃 *Siblings pole aanu. Ithoke avoid cheyyu. Sariyakum 'Chetta/Chechi' vilikkum.*"
}

if st.button("Check Proposal Success 💌"):
    if your_name.strip() == "" or crush_name.strip() == "":
        st.error("Myre! Fill both names before checking.")
    else:
        result = flames_result(your_name, crush_name)
        message = naadan_flames[result]

        st.subheader(f"Result: {result}")
        st.write(message)
