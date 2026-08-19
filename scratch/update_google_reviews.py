import os
import re

REAL_REVIEWS = [
    {
        "name": "Varun Singhal",
        "role": "Verified Google Reviewer (12 reviews)",
        "bg": "#4285F4",
        "color": "#fff",
        "text": "The Credit Lane is a reliable and professional advisory firm specializing in loans and financial solutions. They offer personalized guidance to individuals and businesses seeking the best loan options, including personal & business loans. Highly recommended for trusted loan advice."
    },
    {
        "name": "Vipul Khandelwal",
        "role": "Verified Google Reviewer (13 reviews)",
        "bg": "#34A853",
        "color": "#fff",
        "text": "CA Rajat Garg is very Knowledgeable and professional in his work. Would highly recommend anyone to use his services. Very Happy with the quick response of Team The Credit Lane, they are one of the best Loan advisor."
    },
    {
        "name": "Chandeshwar Sharma",
        "role": "Verified Google Reviewer",
        "bg": "#FBBC05",
        "color": "#000",
        "text": "Expanding my business required additional funds, but finding the right business loan felt overwhelming. With their expertise and personalized guidance, they made the entire process smooth and seamless."
    },
    {
        "name": "Shubham Chaudhary",
        "role": "Verified Google Reviewer (4 reviews)",
        "bg": "#EA4335",
        "color": "#fff",
        "text": "Managing the finances of my business was becoming a challenge, especially when it came to securing a working capital limit. His proactive approach and tailored solutions simplified our entire funding process."
    },
    {
        "name": "Siddarth Sharma",
        "role": "Local Guide (18 reviews)",
        "bg": "#8E44AD",
        "color": "#fff",
        "text": "Highly confident and highly delighted with the services of Credit Lane. Due diligence in place and most importantly the professional ethos driving the team."
    },
    {
        "name": "Ashima Goel",
        "role": "Verified Google Reviewer (5 reviews)",
        "bg": "#16A085",
        "color": "#fff",
        "text": "A one point solution for all professional services with highly qualified professionals in Ghaziabad. They provide prompt and high quality business consulting services."
    },
    {
        "name": "Abhay Saxena",
        "role": "Verified Google Reviewer (5 reviews)",
        "bg": "#D35400",
        "color": "#fff",
        "text": "CA Rajat Garg is truly gentleman with lot's of sincerity and dedication towards his work. Highly recommended THE CREDIT LANE for financial requirements."
    },
    {
        "name": "Ankit Tyagi",
        "role": "Local Guide (144 reviews)",
        "bg": "#2C3E50",
        "color": "#fff",
        "text": "I know this team both personally and professionally. They come with lot of experience and can help you with your varied financial asks. Do give them a try!"
    },
    {
        "name": "Dreksh Singhal",
        "role": "Verified Google Reviewer (4 reviews)",
        "bg": "#27AE60",
        "color": "#fff",
        "text": "Very content work. One can easily trust this company, very good work."
    },
    {
        "name": "Avneet Sharma",
        "role": "Verified Google Reviewer (6 reviews)",
        "bg": "#2980B9",
        "color": "#fff",
        "text": "I took service, I am satisfied with their services & staff is very supportive."
    },
    {
        "name": "Classic Bindi",
        "role": "Verified Google Reviewer (2 reviews)",
        "bg": "#8E44AD",
        "color": "#fff",
        "text": "We availed home loan service from THE CREDIT LANE team. Experience was good."
    },
    {
        "name": "Nishat Khan",
        "role": "Verified Google Reviewer",
        "bg": "#C0392B",
        "color": "#fff",
        "text": "Highly qualified professionals that provides the smooth and best service."
    },
    {
        "name": "Subodh Tyagi",
        "role": "Verified Google Reviewer (3 reviews)",
        "bg": "#D4AC0D",
        "color": "#000",
        "text": "My experience with Credit Lane was topclass. I got the funding of Rs. 50 lacs that helped me to increase my turnover."
    },
    {
        "name": "Mayank Tyagi",
        "role": "Verified Google Reviewer (6 reviews)",
        "bg": "#1ABC9C",
        "color": "#fff",
        "text": "Best credit facility in the area, they are very supportive. You will get the loan quickly."
    },
    {
        "name": "Akash Srivastava",
        "role": "Verified Google Reviewer (13 reviews)",
        "bg": "#34495E",
        "color": "#fff",
        "text": "Very honest and dedicated company who always believes in customer satisfaction."
    },
    {
        "name": "Mandeep Malik",
        "role": "Verified Google Reviewer (2 reviews)",
        "bg": "#E67E22",
        "color": "#fff",
        "text": "50 lakh funding without any security. The whole experience was great."
    },
    {
        "name": "Harsh",
        "role": "Verified Google Reviewer (2 reviews)",
        "bg": "#9B59B6",
        "color": "#fff",
        "text": "Outstanding service. Quick, efficient and impeccable. Highly recommend."
    },
    {
        "name": "Sumit Goel",
        "role": "Verified Google Reviewer (5 reviews)",
        "bg": "#3498DB",
        "color": "#fff",
        "text": "Best team, Very easy process and quick to resolve."
    },
    {
        "name": "G",
        "role": "Verified Google Reviewer (4 reviews)",
        "bg": "#F39C12",
        "color": "#000",
        "text": "Genuine Advice, Genuine People and Genuine Work... rare combination... great experience working with the team."
    },
    {
        "name": "Atul Raj",
        "role": "Verified Google Reviewer (4 reviews)",
        "bg": "#E74C3C",
        "color": "#fff",
        "text": "This company is very useful for loan, I highly recommend visiting this if you need loan."
    },
    {
        "name": "Ajay Anand Sharma",
        "role": "Verified Google Reviewer (9 reviews)",
        "bg": "#16A085",
        "color": "#fff",
        "text": "I am happy with the services. Thank you!"
    },
    {
        "name": "Ankit Kumar Ak",
        "role": "Local Guide (26 reviews)",
        "bg": "#2980B9",
        "color": "#fff",
        "text": "Have a nice experience. Easy way to get knowledge about financial services and loan."
    },
    {
        "name": "Chetan Awal",
        "role": "Verified Google Reviewer (4 reviews)",
        "bg": "#8E44AD",
        "color": "#fff",
        "text": "Very experienced and specialised in terms of service."
    },
    {
        "name": "Puneet Kumar",
        "role": "Verified Google Reviewer (2 reviews)",
        "bg": "#27AE60",
        "color": "#fff",
        "text": "Provides one stop solution to all your Business Finance needs."
    },
    {
        "name": "Rahul Goyal",
        "role": "Verified Google Reviewer (3 reviews)",
        "bg": "#D35400",
        "color": "#fff",
        "text": "Excellent Services and recommended to others."
    },
    {
        "name": "Rishabh Goel",
        "role": "Verified Google Reviewer (3 reviews)",
        "bg": "#2C3E50",
        "color": "#fff",
        "text": "It is very very good provider of loan."
    },
    {
        "name": "Jitendra Kumar",
        "role": "Local Guide (8 reviews)",
        "bg": "#16A085",
        "color": "#fff",
        "text": "Best Services Provided Here."
    },
    {
        "name": "Akshay Agarwal",
        "role": "Verified Google Reviewer (6 reviews)",
        "bg": "#E67E22",
        "color": "#fff",
        "text": "Proactive team with trustworthy functioning."
    },
    {
        "name": "Vivek Prasad",
        "role": "Verified Google Reviewer (7 reviews)",
        "bg": "#2980B9",
        "color": "#fff",
        "text": "Well educated and experienced people."
    },
    {
        "name": "Surbhi Garg",
        "role": "Verified Google Reviewer (4 reviews)",
        "bg": "#9B59B6",
        "color": "#fff",
        "text": "Best service provider for loan."
    }
]

def generate_review_card(r, idx):
    initial = r["name"][0].upper()
    return f"""
            <!-- Card {idx+1} -->
            <div class="review-slide-card" style="flex: 0 0 320px; width: 320px; background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 16px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px;">
                  <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="width: 44px; height: 44px; border-radius: 50%; background: {r['bg']}; color: {r.get('color', '#fff')}; font-weight: 700; display: flex; align-items: center; justify-content: center; font-size: 16px; flex-shrink: 0;">{initial}</div>
                    <div>
                      <h4 style="color: #fff; font-size: 15px; margin: 0 0 3px 0; font-weight: 600;">{r['name']}</h4>
                      <span style="color: #94A3B8; font-size: 12px; display: block;">{r['role']}</span>
                    </div>
                  </div>
                  <svg width="22" height="22" viewBox="0 0 24 24" style="flex-shrink: 0;"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/></svg>
                </div>
                <div style="color: #FFD700; font-size: 15px; margin-bottom: 12px;">★★★★★</div>
                <p style="color: #CBD5E1; font-size: 13.5px; line-height: 1.6; margin: 0;">"{r['text']}"</p>
              </div>
            </div>"""

all_cards_html = "\n".join([generate_review_card(r, i) for i, r in enumerate(REAL_REVIEWS)])

# 1. Update build.py
with open("build.py", "r", encoding="utf-8") as f:
    build_code = f.read()

pattern = r'(<div class="reviews-carousel-track" style="display: flex; gap: 24px; transition: transform 0.4s cubic-bezier\(0.25, 1, 0.5, 1\); will-change: transform;">).*?(</div>\s*</div>\s*</div>\s*</section>)'
new_track_section = r'\1\n' + all_cards_html + r'\n          \2'

updated_build = re.sub(pattern, new_track_section, build_code, flags=re.DOTALL)
with open("build.py", "w", encoding="utf-8") as f:
    f.write(updated_build)
print("Updated build.py with 30 real Google Reviews!")

# 2. Update credit-lane-theme/footer.php
with open("credit-lane-theme/footer.php", "r", encoding="utf-8") as f:
    footer_code = f.read()

updated_footer = re.sub(pattern, new_track_section, footer_code, flags=re.DOTALL)
with open("credit-lane-theme/footer.php", "w", encoding="utf-8") as f:
    f.write(updated_footer)
print("Updated footer.php with 30 real Google Reviews!")
