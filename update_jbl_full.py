import re

index_path = '/Users/green/Downloads/Takealot JBL Charge 6/index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Title and Breadcrumbs
html = re.sub(r'<title>.*?</title>', '<title>JBL Charge 6 Portable Waterproof Bluetooth Speaker with Built-in Powerbank | Takealot</title>', html, flags=re.DOTALL)
html = html.replace('Home / Kitchen & Large Appliances / Small Appliances / Specialty Appliances & Snack Makers / Popcorn Makers', 'Home / Electronics / Audio / Portable & Bluetooth Speakers / JBL Portable Audio')
html = html.replace('Popcorn Makers', 'Portable Bluetooth Speakers')
html = html.replace('Specialty Appliances & Snack Makers', 'Audio & Speakers')
html = html.replace('Kitchen & Small Appliances', 'Electronics')

# 2. Main Title & Brand
html = re.sub(r'<h1 class="product-title"[^>]*>.*?</h1>', '<h1 class="product-title" id="main-product-title">JBL Charge 6 Portable Waterproof Bluetooth Speaker with Built-in Powerbank (Original JBL Pro Sound)</h1>', html, flags=re.DOTALL)
html = re.sub(r'<a href="#" class="brand-link">.*?</a>', '<a href="#" class="brand-link">JBL</a>', html)

# 3. Main Gallery Images
html = re.sub(r'imagens/popcorn_maker_1_hero\.jpg', 'imagens/jbl_charge_1_hero.jpg', html)
html = re.sub(r'imagens/popcorn_maker_2_serving\.jpg', 'imagens/jbl_charge_2_angle.jpg', html)
html = re.sub(r'imagens/popcorn_maker_3_detail\.jpg', 'imagens/jbl_charge_3_radiators.jpg', html)
html = re.sub(r'imagens/popcorn_maker_4_packshot\.jpg', 'imagens/jbl_charge_4_ports.jpg', html)
html = re.sub(r'https://iili\.io/oKbfvVe\.jpg', 'https://iili.io/oKbNUBV.jpg', html)
html = re.sub(r'https://iili\.io/oKbfUKb\.jpg', 'https://iili.io/oKbN621.jpg', html)
html = re.sub(r'https://iili\.io/oKbfglj\.jpg', 'https://iili.io/oKbNtQR.jpg', html)
html = re.sub(r'https://iili\.io/oKbfrUx\.jpg', 'https://iili.io/oKbOHYX.jpg', html)

# 4. Pricing
html = re.sub(r'id="main-price-display">.*?</span>', 'id="main-price-display">R 999</span>', html)
html = re.sub(r'id="main-old-price">.*?</span>', 'id="main-old-price">R 3,999</span>', html)
html = html.replace('R 499', 'R 999')
html = html.replace('R 1,999', 'R 3,999')
html = html.replace('R 1999', 'R 3,999')
html = html.replace('1,500', '3,000')

# 5. Variation Selector Pills
var_pills_html = '''    <!-- Product Variation / Color & Bundle Selector -->
    <div class="variation-selector-sec">
        <div class="variation-header-row">
            <span>Colour / Bundle: <strong id="selected-size-label">Midnight Black (JBL Hero)</strong></span>
            <span style="font-size: 11.5px; color: var(--takealot-blue); font-weight: 600;"><i class="fas fa-sliders" style="margin-right: 3px;"></i> Choose variant</span>
        </div>
        <div class="variation-pills-row">
            <button class="var-pill active" data-var-key="charge-black" onclick="selectProductVariation('charge-black')">
                Midnight Black <span class="pill-badge" style="background: #007a3d;">Hot R 999</span>
            </button>
            <button class="var-pill" data-var-key="charge-teal" onclick="selectProductVariation('charge-teal')">
                Ocean Teal Blue <span class="pill-badge">R 999</span>
            </button>
            <button class="var-pill" data-var-key="charge-camo" onclick="selectProductVariation('charge-camo')">
                Squad Camouflage <span class="pill-badge">R 1,049</span>
            </button>
            <button class="var-pill" data-var-key="charge-duo" onclick="selectProductVariation('charge-duo')">
                Duo Stereo Pack (2x) <span class="pill-badge">R 1,899</span>
            </button>
            <button class="var-pill" data-var-key="flip-compact" onclick="selectProductVariation('flip-compact')">
                JBL Flip 6 Compact <span class="pill-badge">R 699</span>
            </button>
        </div>
    </div>'''

html = re.sub(r'<!-- Product Variation / Model Selector -->.*?<!-- 6\. TakealotMORE Banner', var_pills_html + '\n\n    <!-- 6. TakealotMORE Banner', html, flags=re.DOTALL)

# 6. What's Hot Carousel
hot_carousel_html = '''        <!-- 7. What's Hot in Portable Bluetooth Speakers -->
    <div class="category-hot-sec">
        <div class="sec-title" style="margin-bottom: 12px;">What\'s Hot in Portable Bluetooth Speakers</div>
        <div class="hot-carousel">
            <!-- Variation 1: Midnight Black Hero -->
            <div class="hot-card active-selection" data-var-key="charge-black" onclick="selectProductVariation('charge-black', true)">
                <div class="hot-badges">
                    <div class="badge-black">Top<br>Seller.</div>
                    <div class="badge-blue">75%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/jbl_charge_1_hero.jpg" alt="JBL Charge 6 Midnight Black" />
                </div>
                <div class="hot-title">JBL Charge 6 Portable Waterproof Bluetooth Speaker - Midnight Black</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 999</span>
                    <span class="hot-old-price">R 3,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (4,180)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 2: Ocean Teal Blue -->
            <div class="hot-card" data-var-key="charge-teal" onclick="selectProductVariation('charge-teal', true)">
                <div class="hot-badges">
                    <div class="badge-black">Black<br>November.</div>
                    <div class="badge-blue">75%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/jbl_charge_2_angle.jpg" alt="JBL Charge 6 Ocean Teal Blue" />
                </div>
                <div class="hot-title">JBL Charge 6 Portable Waterproof Bluetooth Speaker - Ocean Teal Blue</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 999</span>
                    <span class="hot-old-price">R 3,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (2,910)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 3: Squad Camouflage -->
            <div class="hot-card" data-var-key="charge-camo" onclick="selectProductVariation('charge-camo', true)">
                <div class="hot-badges">
                    <div class="badge-black">Special<br>Edition</div>
                    <div class="badge-blue">75%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/jbl_charge_3_radiators.jpg" alt="JBL Charge 6 Squad Camouflage" />
                </div>
                <div class="hot-title">JBL Charge 6 Waterproof Bluetooth Speaker - Squad Camouflage Edition</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 1,049</span>
                    <span class="hot-old-price">R 4,199</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.8 (1,430)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 4: Duo Stereo Pack -->
            <div class="hot-card" data-var-key="charge-duo" onclick="selectProductVariation('charge-duo', true)">
                <div class="hot-badges">
                    <div class="badge-black">Stereo<br>Duo</div>
                    <div class="badge-blue">76%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/jbl_charge_4_ports.jpg" alt="JBL Charge 6 Duo Pack Stereo Pair" />
                </div>
                <div class="hot-title">JBL Charge 6 Duo Pack (2x Speakers with Wireless Auracast Stereo Link)</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 1,899</span>
                    <span class="hot-old-price">R 7,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (820)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 5: Flip 6 Compact -->
            <div class="hot-card" data-var-key="flip-compact" onclick="selectProductVariation('flip-compact', true)">
                <div class="hot-badges">
                    <div class="badge-black">Ultra<br>Portable</div>
                    <div class="badge-blue">75%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/jbl_charge_1_hero.jpg" alt="JBL Flip 6 Compact Speaker" />
                </div>
                <div class="hot-title">JBL Flip 6 Compact Waterproof Bluetooth Speaker - Midnight Black</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 699</span>
                    <span class="hot-old-price">R 2,799</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.8 (3,650)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>
        </div>
    </div>'''

html = re.sub(r'<!-- 7\. What\'s Hot in Popcorn Makers -->.*?<!-- 8\. Sold By Section', hot_carousel_html + '\n\n    <div class="divider"></div>\n\n    <!-- 8. Sold By Section', html, flags=re.DOTALL)

# 7. Sold By Section
html = html.replace('Sold by <a href="#">Milex South Africa</a>', 'Sold by <a href="#">JBL South Africa (Harman International)</a>')

# 8. Specifications Table
specs_html = '''        <!-- 14. Product Information -->
    <div class="spec-sec">
        <div class="sec-title">Product Information</div>
        <table class="spec-table">
            <tr>
                <td class="col-label">Categories</td>
                <td class="col-val"><a href="#">Electronics</a> / <a href="#">Audio &amp; Speakers</a> / <a href="#">Portable Bluetooth Speakers</a></td>
            </tr>
            <tr>
                <td class="col-label">Brand</td>
                <td class="col-val"><a href="#">JBL (Harman)</a></td>
            </tr>
            <tr>
                <td class="col-label">Warranty</td>
                <td class="col-val">12-Month Official JBL South Africa Warranty</td>
            </tr>
            <tr>
                <td class="col-label">Output Power</td>
                <td class="col-val" id="spec-capacity">40W RMS (30W Racetrack Woofer + 10W Dome Tweeter)</td>
            </tr>
            <tr>
                <td class="col-label">Model Number</td>
                <td class="col-val" id="spec-model-number">JBLCHARGE6BLK</td>
            </tr>
            <!-- Extra spec rows that expand on Show More -->
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Sound Signature</td>
                <td class="col-val">JBL Original Pro Sound with Dual Pumping Passive Bass Radiators</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Battery Capacity</td>
                <td class="col-val">7,500 mAh Li-ion Rechargeable Battery (27Wh)</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Playtime</td>
                <td class="col-val">Up to 20 Hours of continuous high-volume playtime</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Powerbank Feature</td>
                <td class="col-val">Yes (USB-A 5V/2.0A Out to charge smartphones &amp; devices)</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Water &amp; Dust Proofing</td>
                <td class="col-val">IP67 Certified (Submersible up to 1 meter for 30 minutes)</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Wireless Connectivity</td>
                <td class="col-val">Bluetooth 5.3 + Auracast™ &amp; PartyBoost Multi-Speaker Link</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Charging Interface</td>
                <td class="col-val">USB-C Fast Charge (Full recharge in ~4 hours with 5V/3A)</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Frequency Response</td>
                <td class="col-val">56 Hz - 20,000 Hz</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Transducers</td>
                <td class="col-val">52 x 90 mm Racetrack Woofer + 20 mm Tweeter + Dual Bass Radiators</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Dimensions (W x H x D)</td>
                <td class="col-val">22.3 cm x 9.65 cm x 9.4 cm</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Weight</td>
                <td class="col-val">960 g</td>
            </tr>
        </table>
        <button class="pill-show-more" id="spec-toggle-btn" onclick="toggleSpecs()">Show More</button>
    </div>'''

html = re.sub(r'<!-- 14\. Product Information -->.*?<div class="divider"></div>\s*<!-- 15\. Reviews', specs_html + '\n\n    <div class="divider"></div>\n\n    <!-- 15. Reviews', html, flags=re.DOTALL)

# 9. 14 Authentic South African Reviews
reviews_html = '''        <div id="reviews-list-container">
            <!-- Review 1 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Kagiso Sithole - 26 Sep 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">54</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">The bass on this speaker is absurdly good for its size! Dual passive radiators vibrate the whole table...</span>
                    <span class="review-full" style="display: none;">The bass on this speaker is absurdly good for its size! Dual passive radiators vibrate the whole table during our weekend braais in Sandton. The separate tweeter makes vocal clarity razor-sharp. Battery easily lasted from Saturday afternoon until Sunday evening without needing a single charge. 10/10 purchase!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 2 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Liam van der Merwe - 18 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">42</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">True IP67 waterproofing! Dropped it accidentally in the pool at Clifton 4th beach and it floated and kept playing...</span>
                    <span class="review-full" style="display: none;">True IP67 waterproofing! Dropped it accidentally in the pool at Clifton 4th beach and it floated and kept playing music without missing a single beat. The rugged rubber housing protects against sand and drops. Super fast delivery by Takealot next morning.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 3 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Nompumelelo Dlamini - 04 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">37</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">The built-in powerbank saved my phone during stage 4 loadshedding! Charged my iPhone from 12% to 100%...</span>
                    <span class="review-full" style="display: none;">The built-in powerbank saved my phone during stage 4 loadshedding! Charged my iPhone from 12% to 100% while still streaming Amapiano playlist at 60% volume. It has become an essential device for power cuts and road trips. Highly recommended!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 4 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Jacques Du Plessis - 29 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">29</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Grabbed this on the Takealot Black November deal for R999 instead of R4k. Best audio bargain of the year...</span>
                    <span class="review-full" style="display: none;">Grabbed this on the Takealot Black November deal for R999 instead of R4k. Best audio bargain of the year by far. Original JBL Pro sound with punchy sub-bass you can feel in your chest. Delivered to Pretoria East in less than 24 hours.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 5 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Amina Patel - 12 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">33</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Auracast and PartyBoost stereo pairing works like magic. Linked it with my brothers Charge and the sound was stadium level...</span>
                    <span class="review-full" style="display: none;">Auracast and PartyBoost stereo pairing works like magic. Linked it with my brothers Charge and the sound was stadium level across our entire garden in Umhlanga. Zero audio lag or latency when streaming from Spotify over Bluetooth 5.3.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 6 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Brendan Fourie - 08 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">25</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Took this camping in the Kruger National Park for 4 days. Endured dust, direct heat, and bushveld conditions...</span>
                    <span class="review-full" style="display: none;">Took this camping in the Kruger National Park for 4 days. Endured dust, direct heat, and bushveld conditions without a scratch. Still had 40% battery when we drove back home to Joburg. Indestructible build quality from Harman.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 7 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Thabo Mokoena - 22 Sep 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">21</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Volume is mind-blowing. At 70% volume it fills a massive double garage and outdoor patio easily...</span>
                    <span class="review-full" style="display: none;">Volume is mind-blowing. At 70% volume it fills a massive double garage and outdoor patio easily without any audio distortion. The bass never gets muddy even with heavy hip hop or EDM. Truly the king of portable speakers.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 8 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Chloe Botha - 15 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">27</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">The Ocean Teal Blue colorway is gorgeous in person. Texture is premium and feels very comfortable in hand...</span>
                    <span class="review-full" style="display: none;">The Ocean Teal Blue colorway is gorgeous in person. Texture is premium and feels very comfortable in hand. USB-C fast charging works with my standard MacBook charger so I only need to carry one cable. Arrived in pristine condition in Ballito.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 9 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Sipho Khumalo - 01 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">19</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Upgraded from my old Charge 3. The leap in soundstage clarity and power output with the 40W system is night and day...</span>
                    <span class="review-full" style="display: none;">Upgraded from my old Charge 3. The leap in soundstage clarity and power output with the 40W system is night and day. Podcasting voices are super crisp and Deep House tracks sound studio mastered. Worth every single cent.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 10 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Megan Oosthuizen - 20 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">31</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Great companion for beach workouts in Sea Point. Sand rinses right off under the tap without issue...</span>
                    <span class="review-full" style="display: none;">Great companion for beach workouts in Sea Point. Sand rinses right off under the tap without issue thanks to the sealed IP67 rating. The Bluetooth range stays locked even when walking 20 meters away with my phone. Best portable audio purchase!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 11 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Gareth Naidoo - 28 Sep 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">16</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Bought this as a 21st birthday gift for my nephew. He was ecstatic! Connects instantly to iPhone and Android...</span>
                    <span class="review-full" style="display: none;">Bought this as a 21st birthday gift for my nephew. He was ecstatic! Connects instantly to iPhone and Android devices. The JBL One app lets you customize the 3-band equalizer to your exact taste. Authentic JBL South Africa stock with serial verification.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 12 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Zanele Ndlovu - 10 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">38</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Battery life is unbelievable. Used it daily for 2 hours during kitchen cooking and chores for two weeks on a single charge...</span>
                    <span class="review-full" style="display: none;">Battery life is unbelievable. Used it daily for 2 hours during kitchen cooking and chores for two weeks on a single charge. The battery indicator LED bar gives you clear visual remaining percentage. Superb design and ruggedness.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 13 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Dirk Coetzee - 17 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">23</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Pairs perfectly with our outdoor cinema projector. Low latency means audio and mouth movements sync seamlessly...</span>
                    <span class="review-full" style="display: none;">Pairs perfectly with our outdoor cinema projector. Low latency means audio and mouth movements sync seamlessly without any echo or delay. The explosions and action scenes sound like a mini movie theater in our backyard in Durbanville.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 14 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Farhana Cassim - 05 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">41</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Top quality Harman engineering. Everything about this speaker feels heavy-duty, premium and built to last...</span>
                    <span class="review-full" style="display: none;">Top quality Harman engineering. Everything about this speaker feels heavy-duty, premium and built to last for many years. Sound doesn\'t crackle even at maximum volume. Takealot delivery was punctual and well packaged. Best purchase of 2026!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>
        </div>'''

html = re.sub(r'<div id="reviews-list-container">.*?</div>\s*<button class="load-more-reviews-btn"', reviews_html + '\n\n        <button class="load-more-reviews-btn"', html, flags=re.DOTALL)

# 10. JavaScript Variations Object
js_variations_code = '''    // Product Variations Data Dictionary (JBL Charge 6)
    const productVariations = {
        'charge-black': {
            title: 'JBL Charge 6 Portable Waterproof Bluetooth Speaker - Midnight Black',
            label: 'Midnight Black (JBL Hero)',
            price: 999,
            oldPrice: 3999,
            discount: '75%',
            image: 'imagens/jbl_charge_1_hero.jpg',
            capacity: '40W RMS / 20 Hours Playtime + Powerbank',
            modelNumber: 'JBLCHARGE6BLK',
            rating: '4.9 (4,180)',
            reviewsCount: '4,180'
        },
        'charge-teal': {
            title: 'JBL Charge 6 Portable Waterproof Bluetooth Speaker - Ocean Teal Blue',
            label: 'Ocean Teal Blue',
            price: 999,
            oldPrice: 3999,
            discount: '75%',
            image: 'imagens/jbl_charge_2_angle.jpg',
            capacity: '40W RMS / 20 Hours Playtime + Powerbank',
            modelNumber: 'JBLCHARGE6TEAL',
            rating: '4.9 (2,910)',
            reviewsCount: '2,910'
        },
        'charge-camo': {
            title: 'JBL Charge 6 Waterproof Bluetooth Speaker - Squad Camouflage Edition',
            label: 'Squad Camouflage Edition',
            price: 1049,
            oldPrice: 4199,
            discount: '75%',
            image: 'imagens/jbl_charge_3_radiators.jpg',
            capacity: '40W RMS / Rugged Outdoor Camo Finish',
            modelNumber: 'JBLCHARGE6CAMO',
            rating: '4.8 (1,430)',
            reviewsCount: '1,430'
        },
        'charge-duo': {
            title: 'JBL Charge 6 Duo Pack (2x Speakers with Wireless Auracast Stereo Link)',
            label: 'Duo Stereo Pack (2x Speakers)',
            price: 1899,
            oldPrice: 7999,
            discount: '76%',
            image: 'imagens/jbl_charge_4_ports.jpg',
            capacity: '2x 40W (80W Total) True Wireless Stereo Pair',
            modelNumber: 'JBLCHARGE6-DUO',
            rating: '4.9 (820)',
            reviewsCount: '820'
        },
        'flip-compact': {
            title: 'JBL Flip 6 Compact Waterproof Bluetooth Speaker - Midnight Black',
            label: 'JBL Flip 6 Compact',
            price: 699,
            oldPrice: 2799,
            discount: '75%',
            image: 'imagens/jbl_charge_1_hero.jpg',
            capacity: '30W RMS / Ultra-Portable 12h Playtime',
            modelNumber: 'JBLFLIP6BLK',
            rating: '4.8 (3,650)',
            reviewsCount: '3,650'
        }
    };'''

html = re.sub(r'// Product Variations Data Dictionary.*?const productVariations = \{.*?\};', js_variations_code, html, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('JBL Charge 6 index.html full update complete!')
