import os, re

# ==============================================================
# 1. FIX POPCORN MAKER (index.html, cart.html)
# ==============================================================
popcorn_dir = '/Users/green/Downloads/Takealot Popcorn Maker'
popcorn_index = os.path.join(popcorn_dir, 'index.html')
with open(popcorn_index, 'r', encoding='utf-8') as f:
    p_html = f.read()

# Fix initial state
p_html = re.sub(r'let selectedVariationKey\s*=\s*"[^"]*";', 'let selectedVariationKey = "milex-retro";', p_html)
p_html = re.sub(r'let selectedPrice\s*=\s*[^;]+;', 'let selectedPrice = 499;', p_html)
p_html = re.sub(r'let selectedTitle\s*=\s*"[^"]*";', 'let selectedTitle = "Milex Retro Popcorn Maker - Hot Air Popcorn Machine | Vintage Cinema Style (MRP001)";', p_html)
p_html = re.sub(r'let selectedImage\s*=\s*"[^"]*";', 'let selectedImage = "imagens/popcorn_maker_1_hero.jpg";', p_html)

# Update productVariations in Popcorn Maker
popcorn_variations = """    // Product Variations Data Dictionary (Popcorn Makers)
    const productVariations = {
        'compact-1200w': {
            id: 'compact-1200w',
            size: 'Compact 1200W Hot Air',
            title: 'Compact 1200W Electric Hot Air Popcorn Popper (Oil-Free)',
            price: 299,
            oldPrice: 'R 1,199',
            discount: '75%<br>OFF',
            credit: 'R 25 p/m x 12 months',
            ebucks: 'eB2,990',
            miles: '2,990',
            image: 'imagens/popcorn_maker_3_detail.jpg',
            images: [
                'imagens/popcorn_maker_3_detail.jpg',
                'imagens/popcorn_maker_1_hero.jpg',
                'imagens/popcorn_maker_2_serving.jpg',
                'imagens/popcorn_maker_4_packshot.jpg'
            ],
            screenSizeSpec: '1200W Rapid Vortex (Oil-Free)',
            modelSpec: 'HP-1200-MINI'
        },
        'milex-retro': {
            id: 'milex-retro',
            size: 'Retro Cinema Style (Milex Hero)',
            title: 'Milex Retro Popcorn Maker - Hot Air Popcorn Machine | Vintage Cinema Style (MRP001)',
            price: 499,
            oldPrice: 'R 1,999',
            discount: '75%<br>OFF',
            credit: 'R 42 p/m x 12 months',
            ebucks: 'eB4,990',
            miles: '4,990',
            image: 'imagens/popcorn_maker_1_hero.jpg',
            images: [
                'imagens/popcorn_maker_1_hero.jpg',
                'imagens/popcorn_maker_2_serving.jpg',
                'imagens/popcorn_maker_3_detail.jpg',
                'imagens/popcorn_maker_4_packshot.jpg'
            ],
            screenSizeSpec: 'Up to 60 Litres / Hour (16 Cups)',
            modelSpec: 'MRP001'
        },
        'deluxe-kit': {
            id: 'deluxe-kit',
            size: 'Deluxe Kit + 1kg Kernels & 4 Flavours',
            title: 'Milex Retro Popcorn Maker + 1kg Non-GMO Kernels & 4 Cinema Flavour Shakers Kit',
            price: 599,
            oldPrice: 'R 2,499',
            discount: '76%<br>OFF',
            credit: 'R 50 p/m x 12 months',
            ebucks: 'eB5,990',
            miles: '5,990',
            image: 'imagens/popcorn_maker_2_serving.jpg',
            images: [
                'imagens/popcorn_maker_2_serving.jpg',
                'imagens/popcorn_maker_1_hero.jpg',
                'imagens/popcorn_maker_3_detail.jpg',
                'imagens/popcorn_maker_4_packshot.jpg'
            ],
            screenSizeSpec: 'Full Cinema Kit + 1kg Gourmet Corn + 4 Shakers',
            modelSpec: 'MRP001-BNDL'
        },
        'commercial-8oz': {
            id: 'commercial-8oz',
            size: 'Commercial 8oz Vintage Cart',
            title: 'Commercial 8oz Vintage Cart High-Capacity Popcorn Machine',
            price: 999,
            oldPrice: 'R 4,999',
            discount: '80%<br>OFF',
            credit: 'R 83 p/m x 12 months',
            ebucks: 'eB9,990',
            miles: '9,990',
            image: 'imagens/popcorn_maker_4_packshot.jpg',
            images: [
                'imagens/popcorn_maker_4_packshot.jpg',
                'imagens/popcorn_maker_1_hero.jpg',
                'imagens/popcorn_maker_2_serving.jpg',
                'imagens/popcorn_maker_3_detail.jpg'
            ],
            screenSizeSpec: 'Commercial 8oz Kettle / 120L per hour',
            modelSpec: 'CPM-800-CART'
        }
    };"""

p_html = re.sub(r'const productVariations\s*=\s*\{.*?\n    \};', popcorn_variations, p_html, flags=re.DOTALL)

# Update selectProductVariation function
popcorn_select_fn = """    function selectProductVariation(varKey, shouldScroll) {
        const item = productVariations[varKey];
        if (!item) return;

        selectedVariationKey = varKey;
        selectedPrice = item.price;
        selectedTitle = item.title;
        selectedImage = item.image;

        const formattedPrice = parseInt(item.price).toLocaleString("en-ZA");

        // 1. Update Title
        const titleEl = document.getElementById('main-product-title');
        if (titleEl) titleEl.textContent = item.title;

        // 2. Update Prices
        const priceDisplay = document.getElementById('main-price-display');
        if (priceDisplay) priceDisplay.textContent = 'R ' + formattedPrice;
        const footerPrice = document.getElementById('footer-price-display');
        if (footerPrice) footerPrice.textContent = 'R ' + formattedPrice;
        const oldPriceEl = document.getElementById('main-old-price');
        if (oldPriceEl) oldPriceEl.textContent = item.oldPrice;

        // 3. Update Discount Badge
        const discountBadge = document.getElementById('main-discount-badge');
        if (discountBadge) discountBadge.innerHTML = item.discount;

        // 4. Update Credit & Rewards
        const creditEl = document.getElementById('credit-installment');
        if (creditEl) creditEl.textContent = item.credit;
        const ebucksEl = document.getElementById('reward-ebucks-val');
        if (ebucksEl) ebucksEl.textContent = item.ebucks;
        const milesEl = document.getElementById('reward-miles-val');
        if (milesEl) milesEl.textContent = item.miles;

        // 5. Update Spec Table
        const specCapacity = document.getElementById('spec-capacity');
        if (specCapacity) specCapacity.textContent = item.screenSizeSpec;
        const specModel = document.getElementById('spec-model-number');
        if (specModel) specModel.textContent = item.modelSpec;

        // 6. Update Size / Model Label
        const sizeLabel = document.getElementById('selected-size-label');
        if (sizeLabel) sizeLabel.textContent = item.size;

        // 7. Update Active Pill
        document.querySelectorAll('.var-pill').forEach(pill => {
            pill.classList.toggle('active', pill.getAttribute('data-var-key') === varKey);
        });

        // 8. Update Active Hot Card
        document.querySelectorAll('.hot-card').forEach(card => {
            card.classList.toggle('active-selection', card.getAttribute('data-var-key') === varKey);
        });

        // 9. Update carousel slide 1 with selected item image
        if (item.images && item.images.length) {
            const slideImgs = document.querySelectorAll('#carousel .carousel-slide img');
            slideImgs.forEach((img, idx) => {
                if (item.images[idx]) {
                    img.src = item.images[idx];
                    img.alt = item.title + ' - Image ' + (idx + 1);
                }
            });
        }

        // 10. Persist in localStorage
        try {
            localStorage.setItem('takealot_selected_product', JSON.stringify({
                key: varKey,
                title: item.title,
                price: item.price,
                image: item.image,
                size: item.size
            }));
        } catch(e) {}

        showLocationToast('Selected: ' + item.size + ' · R ' + formattedPrice);

        if (shouldScroll) {
            const metaSec = document.querySelector('.product-meta') || document.querySelector('.price-section');
            if (metaSec) {
                metaSec.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    }"""

p_html = re.sub(r'function selectProductVariation\(.*?\)\s*\{.*?\n    \}', popcorn_select_fn, p_html, flags=re.DOTALL)

with open(popcorn_index, 'w', encoding='utf-8') as f:
    f.write(p_html)

# Update Popcorn Maker cart.html
popcorn_cart = os.path.join(popcorn_dir, 'cart.html')
with open(popcorn_cart, 'r', encoding='utf-8') as f:
    p_cart = f.read()

# Make cart item dynamically reflect selected product
p_cart = p_cart.replace(
    '<img src="imagens/popcorn_maker_1_hero.jpg" alt="Samsung 14-Place Freestanding Steel Popcorn Maker (DW60M5070FS)" class="product-thumb" />',
    '<img src="imagens/popcorn_maker_1_hero.jpg" alt="Popcorn Maker" id="cart-item-img" class="product-thumb" />'
)
p_cart = p_cart.replace(
    '<div class="product-title">Milex Retro Cinema Popcorn Maker (MRP001)</div>',
    '<div class="product-title" id="cart-item-title">Milex Retro Cinema Popcorn Maker (MRP001)</div>'
)

# Update cart.html script block to read takealot_selected_product
cart_js_popcorn = """<script>
    let savedProduct = {};
    try {
      savedProduct = JSON.parse(localStorage.getItem('takealot_selected_product') || '{}');
    } catch(e) {}

    function getQueryParam(name) {
      const urlParams = new URLSearchParams(window.location.search);
      return urlParams.get(name);
    }

    const price = getQueryParam("price") || (savedProduct.price ? String(savedProduct.price) : "499");
    const prodTitle = getQueryParam("title") || savedProduct.title || "Milex Retro Cinema Popcorn Maker (MRP001)";
    const prodImg = getQueryParam("img") || savedProduct.image || "imagens/popcorn_maker_1_hero.jpg";

    if (document.getElementById("cart-item-title")) {
      document.getElementById("cart-item-title").textContent = prodTitle;
    }
    if (document.getElementById("cart-item-img")) {
      document.getElementById("cart-item-img").src = prodImg;
    }

    if (price) {
      const formatted = parseInt(price).toLocaleString("en-ZA");
      document.getElementById("price-value").textContent = formatted;
      document.getElementById("price-total").textContent = formatted;
    }

    function proceedToCheckout() {
      window.location.href = `checkout.html?price=${price}&title=${encodeURIComponent(prodTitle)}&img=${encodeURIComponent(prodImg)}`;
    }
  </script>"""

p_cart = re.sub(r'<script>\s*function getQueryParam\(name\).*?</script>', cart_js_popcorn, p_cart, flags=re.DOTALL)
p_cart = re.sub(r'onclick="window\.location\.href\s*=\s*`checkout\.html\?price=\$\{price\}`"', 'onclick="proceedToCheckout()"', p_cart)

with open(popcorn_cart, 'w', encoding='utf-8') as f:
    f.write(p_cart)

print("Popcorn Maker index.html and cart.html updated successfully!")


# ==============================================================
# 2. FIX JBL CHARGE 6 (index.html, cart.html) WITH 5 REAL COLORS
# ==============================================================
jbl_dir = '/Users/green/Downloads/Takealot JBL Charge 6'
jbl_index = os.path.join(jbl_dir, 'index.html')
with open(jbl_index, 'r', encoding='utf-8') as f:
    j_html = f.read()

# Fix initial state for JBL
j_html = re.sub(r'let selectedVariationKey\s*=\s*"[^"]*";', 'let selectedVariationKey = "charge-black";', j_html)
j_html = re.sub(r'let selectedPrice\s*=\s*[^;]+;', 'let selectedPrice = 999;', j_html)
j_html = re.sub(r'let selectedTitle\s*=\s*"[^"]*";', 'let selectedTitle = "JBL Charge 6 Portable Waterproof Bluetooth Speaker - Midnight Black";', j_html)
j_html = re.sub(r'let selectedImage\s*=\s*"[^"]*";', 'let selectedImage = "imagens/jbl_charge_black_1.jpg";', j_html)

# Set Color Variation Pills with realistic color swatches
jbl_color_pills = """    <!-- Product Variation / Color & Bundle Selector -->
    <div class="variation-selector-sec">
        <div class="variation-header-row">
            <span>Colour: <strong id="selected-size-label">Midnight Black (JBL Hero)</strong></span>
            <span style="font-size: 11.5px; color: var(--takealot-blue); font-weight: 600;"><i class="fas fa-palette" style="margin-right: 3px;"></i> Select color</span>
        </div>
        <div class="variation-pills-row">
            <button class="var-pill active" data-var-key="charge-black" onclick="selectProductVariation('charge-black')">
                <span style="background: #111; border: 1.5px solid #666; width: 13px; height: 13px; border-radius: 50%; display: inline-block; margin-right: 6px; vertical-align: middle;"></span>
                Midnight Black <span class="pill-badge" style="background: #007a3d;">Hot R 999</span>
            </button>
            <button class="var-pill" data-var-key="charge-teal" onclick="selectProductVariation('charge-teal')">
                <span style="background: #008b8b; width: 13px; height: 13px; border-radius: 50%; display: inline-block; margin-right: 6px; vertical-align: middle;"></span>
                Ocean Teal <span class="pill-badge">R 999</span>
            </button>
            <button class="var-pill" data-var-key="charge-red" onclick="selectProductVariation('charge-red')">
                <span style="background: #d32f2f; width: 13px; height: 13px; border-radius: 50%; display: inline-block; margin-right: 6px; vertical-align: middle;"></span>
                Fiery Red <span class="pill-badge">R 999</span>
            </button>
            <button class="var-pill" data-var-key="charge-green" onclick="selectProductVariation('charge-green')">
                <span style="background: #2e7d32; width: 13px; height: 13px; border-radius: 50%; display: inline-block; margin-right: 6px; vertical-align: middle;"></span>
                Forest Green <span class="pill-badge">R 999</span>
            </button>
            <button class="var-pill" data-var-key="charge-camo" onclick="selectProductVariation('charge-camo')">
                <span style="background: #556b2f; width: 13px; height: 13px; border-radius: 50%; display: inline-block; margin-right: 6px; vertical-align: middle;"></span>
                Squad Camo <span class="pill-badge">R 1,049</span>
            </button>
            <button class="var-pill" data-var-key="charge-duo" onclick="selectProductVariation('charge-duo')">
                <i class="fas fa-layer-group" style="margin-right: 5px; color: #f5a623;"></i>
                Duo Stereo Pack (2x) <span class="pill-badge">R 1,899</span>
            </button>
        </div>
    </div>"""

j_html = re.sub(r'<!-- Product Variation / Color & Bundle Selector -->.*?<!-- 6\. TakealotMORE Banner', jbl_color_pills + '\n\n    <!-- 6. TakealotMORE Banner', j_html, flags=re.DOTALL)

# Set What's Hot Carousel with exact matching keys
jbl_hot_carousel = """        <!-- 7. What's Hot in Portable Bluetooth Speakers -->
    <div class="category-hot-sec">
        <div class="sec-title" style="margin-bottom: 12px;">What\'s Hot in Portable Bluetooth Speakers</div>
        <div class="hot-carousel">
            <!-- Variation 1: Midnight Black -->
            <div class="hot-card active-selection" data-var-key="charge-black" onclick="selectProductVariation('charge-black', true)">
                <div class="hot-badges">
                    <div class="badge-black">Top<br>Seller.</div>
                    <div class="badge-blue">75%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/jbl_charge_black_1.jpg" alt="JBL Charge 6 Midnight Black" />
                </div>
                <div class="hot-title">JBL Charge 6 Portable Waterproof Bluetooth Speaker - Midnight Black</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 999</span>
                    <span class="hot-old-price">R 3,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (4,180)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 2: Ocean Teal -->
            <div class="hot-card" data-var-key="charge-teal" onclick="selectProductVariation('charge-teal', true)">
                <div class="hot-badges">
                    <div class="badge-black">Ocean<br>Teal</div>
                    <div class="badge-blue">75%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/jbl_charge_teal_1.jpg" alt="JBL Charge 6 Ocean Teal" />
                </div>
                <div class="hot-title">JBL Charge 6 Portable Waterproof Bluetooth Speaker - Ocean Teal</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 999</span>
                    <span class="hot-old-price">R 3,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (2,910)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 3: Fiery Red -->
            <div class="hot-card" data-var-key="charge-red" onclick="selectProductVariation('charge-red', true)">
                <div class="hot-badges">
                    <div class="badge-black">Fiery<br>Red</div>
                    <div class="badge-blue">75%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/jbl_charge_red_1.jpg" alt="JBL Charge 6 Fiery Red" />
                </div>
                <div class="hot-title">JBL Charge 6 Portable Waterproof Bluetooth Speaker - Fiery Red</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 999</span>
                    <span class="hot-old-price">R 3,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (1,850)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 4: Forest Green -->
            <div class="hot-card" data-var-key="charge-green" onclick="selectProductVariation('charge-green', true)">
                <div class="hot-badges">
                    <div class="badge-black">Forest<br>Green</div>
                    <div class="badge-blue">75%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/jbl_charge_green_1.jpg" alt="JBL Charge 6 Forest Green" />
                </div>
                <div class="hot-title">JBL Charge 6 Portable Waterproof Bluetooth Speaker - Forest Green</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 999</span>
                    <span class="hot-old-price">R 3,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (1,120)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 5: Squad Camo -->
            <div class="hot-card" data-var-key="charge-camo" onclick="selectProductVariation('charge-camo', true)">
                <div class="hot-badges">
                    <div class="badge-black">Squad<br>Camo</div>
                    <div class="badge-blue">75%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/jbl_charge_camo_1.jpg" alt="JBL Charge 6 Squad Camouflage" />
                </div>
                <div class="hot-title">JBL Charge 6 Waterproof Bluetooth Speaker - Squad Camouflage Edition</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 1,049</span>
                    <span class="hot-old-price">R 4,199</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.8 (1,430)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 6: Duo Stereo Pack -->
            <div class="hot-card" data-var-key="charge-duo" onclick="selectProductVariation('charge-duo', true)">
                <div class="hot-badges">
                    <div class="badge-black">Stereo<br>Pair</div>
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
        </div>
    </div>"""

j_html = re.sub(r'<!-- 7\. What\'s Hot in Portable Bluetooth Speakers -->.*?<!-- 8\. Sold By Section', jbl_hot_carousel + '\n\n    <div class="divider"></div>\n\n    <!-- 8. Sold By Section', j_html, flags=re.DOTALL)

# Update productVariations in JBL
jbl_variations = """    // Product Variations Data Dictionary (JBL Charge 6 Colors)
    const productVariations = {
        'charge-black': {
            id: 'charge-black',
            size: 'Midnight Black (Hero)',
            title: 'JBL Charge 6 Portable Waterproof Bluetooth Speaker - Midnight Black',
            price: 999,
            oldPrice: 'R 3,999',
            discount: '75%<br>OFF',
            credit: 'R 83 p/m x 12 months',
            ebucks: 'eB9,990',
            miles: '9,990',
            image: 'imagens/jbl_charge_black_1.jpg',
            images: [
                'imagens/jbl_charge_black_1.jpg',
                'imagens/jbl_charge_2_angle.jpg',
                'imagens/jbl_charge_3_radiators.jpg',
                'imagens/jbl_charge_4_ports.jpg'
            ],
            screenSizeSpec: '40W RMS / 20h Battery + Powerbank',
            modelSpec: 'JBLCHARGE6BLK'
        },
        'charge-teal': {
            id: 'charge-teal',
            size: 'Ocean Teal Blue',
            title: 'JBL Charge 6 Portable Waterproof Bluetooth Speaker - Ocean Teal Blue',
            price: 999,
            oldPrice: 'R 3,999',
            discount: '75%<br>OFF',
            credit: 'R 83 p/m x 12 months',
            ebucks: 'eB9,990',
            miles: '9,990',
            image: 'imagens/jbl_charge_teal_1.jpg',
            images: [
                'imagens/jbl_charge_teal_1.jpg',
                'imagens/jbl_charge_2_angle.jpg',
                'imagens/jbl_charge_3_radiators.jpg',
                'imagens/jbl_charge_4_ports.jpg'
            ],
            screenSizeSpec: '40W RMS / Ocean Teal Finish',
            modelSpec: 'JBLCHARGE6TEAL'
        },
        'charge-red': {
            id: 'charge-red',
            size: 'Fiery Red',
            title: 'JBL Charge 6 Portable Waterproof Bluetooth Speaker - Fiery Red',
            price: 999,
            oldPrice: 'R 3,999',
            discount: '75%<br>OFF',
            credit: 'R 83 p/m x 12 months',
            ebucks: 'eB9,990',
            miles: '9,990',
            image: 'imagens/jbl_charge_red_1.jpg',
            images: [
                'imagens/jbl_charge_red_1.jpg',
                'imagens/jbl_charge_2_angle.jpg',
                'imagens/jbl_charge_3_radiators.jpg',
                'imagens/jbl_charge_4_ports.jpg'
            ],
            screenSizeSpec: '40W RMS / Fiery Red Finish',
            modelSpec: 'JBLCHARGE6RED'
        },
        'charge-green': {
            id: 'charge-green',
            size: 'Forest Green',
            title: 'JBL Charge 6 Portable Waterproof Bluetooth Speaker - Forest Green',
            price: 999,
            oldPrice: 'R 3,999',
            discount: '75%<br>OFF',
            credit: 'R 83 p/m x 12 months',
            ebucks: 'eB9,990',
            miles: '9,990',
            image: 'imagens/jbl_charge_green_1.jpg',
            images: [
                'imagens/jbl_charge_green_1.jpg',
                'imagens/jbl_charge_2_angle.jpg',
                'imagens/jbl_charge_3_radiators.jpg',
                'imagens/jbl_charge_4_ports.jpg'
            ],
            screenSizeSpec: '40W RMS / Forest Green Finish',
            modelSpec: 'JBLCHARGE6GRN'
        },
        'charge-camo': {
            id: 'charge-camo',
            size: 'Squad Camouflage',
            title: 'JBL Charge 6 Waterproof Bluetooth Speaker - Squad Camouflage Edition',
            price: 1049,
            oldPrice: 'R 4,199',
            discount: '75%<br>OFF',
            credit: 'R 87 p/m x 12 months',
            ebucks: 'eB10,490',
            miles: '10,490',
            image: 'imagens/jbl_charge_camo_1.jpg',
            images: [
                'imagens/jbl_charge_camo_1.jpg',
                'imagens/jbl_charge_2_angle.jpg',
                'imagens/jbl_charge_3_radiators.jpg',
                'imagens/jbl_charge_4_ports.jpg'
            ],
            screenSizeSpec: '40W RMS / Squad Camouflage Finish',
            modelSpec: 'JBLCHARGE6CAMO'
        },
        'charge-duo': {
            id: 'charge-duo',
            size: 'Duo Stereo Pack (2x Speakers)',
            title: 'JBL Charge 6 Duo Pack (2x Speakers with Wireless Auracast Stereo Link)',
            price: 1899,
            oldPrice: 'R 7,999',
            discount: '76%<br>OFF',
            credit: 'R 158 p/m x 12 months',
            ebucks: 'eB18,990',
            miles: '18,990',
            image: 'imagens/jbl_charge_4_ports.jpg',
            images: [
                'imagens/jbl_charge_4_ports.jpg',
                'imagens/jbl_charge_black_1.jpg',
                'imagens/jbl_charge_teal_1.jpg',
                'imagens/jbl_charge_3_radiators.jpg'
            ],
            screenSizeSpec: '2x 40W (80W Total) True Wireless Stereo Pair',
            modelSpec: 'JBLCHARGE6-DUO'
        }
    };"""

j_html = re.sub(r'const productVariations\s*=\s*\{.*?\n    \};', jbl_variations, j_html, flags=re.DOTALL)

# Update selectProductVariation function for JBL
jbl_select_fn = """    function selectProductVariation(varKey, shouldScroll) {
        const item = productVariations[varKey];
        if (!item) return;

        selectedVariationKey = varKey;
        selectedPrice = item.price;
        selectedTitle = item.title;
        selectedImage = item.image;

        const formattedPrice = parseInt(item.price).toLocaleString("en-ZA");

        // 1. Update Title
        const titleEl = document.getElementById('main-product-title');
        if (titleEl) titleEl.textContent = item.title;

        // 2. Update Prices
        const priceDisplay = document.getElementById('main-price-display');
        if (priceDisplay) priceDisplay.textContent = 'R ' + formattedPrice;
        const footerPrice = document.getElementById('footer-price-display');
        if (footerPrice) footerPrice.textContent = 'R ' + formattedPrice;
        const oldPriceEl = document.getElementById('main-old-price');
        if (oldPriceEl) oldPriceEl.textContent = item.oldPrice;

        // 3. Update Discount Badge
        const discountBadge = document.getElementById('main-discount-badge');
        if (discountBadge) discountBadge.innerHTML = item.discount;

        // 4. Update Credit & Rewards
        const creditEl = document.getElementById('credit-installment');
        if (creditEl) creditEl.textContent = item.credit;
        const ebucksEl = document.getElementById('reward-ebucks-val');
        if (ebucksEl) ebucksEl.textContent = item.ebucks;
        const milesEl = document.getElementById('reward-miles-val');
        if (milesEl) milesEl.textContent = item.miles;

        // 5. Update Spec Table
        const specCapacity = document.getElementById('spec-capacity');
        if (specCapacity) specCapacity.textContent = item.screenSizeSpec;
        const specModel = document.getElementById('spec-model-number');
        if (specModel) specModel.textContent = item.modelSpec;

        // 6. Update Color Label
        const sizeLabel = document.getElementById('selected-size-label');
        if (sizeLabel) sizeLabel.textContent = item.size;

        // 7. Update Active Pill
        document.querySelectorAll('.var-pill').forEach(pill => {
            pill.classList.toggle('active', pill.getAttribute('data-var-key') === varKey);
        });

        // 8. Update Active Hot Card
        document.querySelectorAll('.hot-card').forEach(card => {
            card.classList.toggle('active-selection', card.getAttribute('data-var-key') === varKey);
        });

        // 9. Update carousel slides to match selected color
        if (item.images && item.images.length) {
            const slideImgs = document.querySelectorAll('#carousel .carousel-slide img');
            slideImgs.forEach((img, idx) => {
                if (item.images[idx]) {
                    img.src = item.images[idx];
                    img.alt = item.title + ' - Image ' + (idx + 1);
                }
            });
        }

        // 10. Persist in localStorage
        try {
            localStorage.setItem('takealot_selected_product', JSON.stringify({
                key: varKey,
                title: item.title,
                price: item.price,
                image: item.image,
                size: item.size
            }));
        } catch(e) {}

        showLocationToast('Colour selected: ' + item.size + ' · R ' + formattedPrice);

        if (shouldScroll) {
            const metaSec = document.querySelector('.product-meta') || document.querySelector('.price-section');
            if (metaSec) {
                metaSec.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    }"""

j_html = re.sub(r'function selectProductVariation\(.*?\)\s*\{.*?\n    \}', jbl_select_fn, j_html, flags=re.DOTALL)

with open(jbl_index, 'w', encoding='utf-8') as f:
    f.write(j_html)

# Update JBL cart.html
jbl_cart = os.path.join(jbl_dir, 'cart.html')
with open(jbl_cart, 'r', encoding='utf-8') as f:
    j_cart = f.read()

j_cart = j_cart.replace(
    '<img src="imagens/jbl_charge_1_hero.jpg" alt="Samsung 14-Place Freestanding Steel Popcorn Maker (DW60M5070FS)" class="product-thumb" />',
    '<img src="imagens/jbl_charge_black_1.jpg" alt="JBL Charge 6" id="cart-item-img" class="product-thumb" />'
)
j_cart = re.sub(r'<img src="imagens/jbl_charge_1_hero\.jpg"[^>]*class="product-thumb"[^>]*>', '<img src="imagens/jbl_charge_black_1.jpg" alt="JBL Charge 6" id="cart-item-img" class="product-thumb" />', j_cart)
j_cart = re.sub(r'<div class="product-title"[^>]*>.*?</div>', '<div class="product-title" id="cart-item-title">JBL Charge 6 Portable Waterproof Bluetooth Speaker - Midnight Black</div>', j_cart, count=1)

cart_js_jbl = """<script>
    let savedProduct = {};
    try {
      savedProduct = JSON.parse(localStorage.getItem('takealot_selected_product') || '{}');
    } catch(e) {}

    function getQueryParam(name) {
      const urlParams = new URLSearchParams(window.location.search);
      return urlParams.get(name);
    }

    const price = getQueryParam("price") || (savedProduct.price ? String(savedProduct.price) : "999");
    const prodTitle = getQueryParam("title") || savedProduct.title || "JBL Charge 6 Portable Waterproof Bluetooth Speaker - Midnight Black";
    const prodImg = getQueryParam("img") || savedProduct.image || "imagens/jbl_charge_black_1.jpg";

    if (document.getElementById("cart-item-title")) {
      document.getElementById("cart-item-title").textContent = prodTitle;
    }
    if (document.getElementById("cart-item-img")) {
      document.getElementById("cart-item-img").src = prodImg;
    }

    if (price) {
      const formatted = parseInt(price).toLocaleString("en-ZA");
      document.getElementById("price-value").textContent = formatted;
      document.getElementById("price-total").textContent = formatted;
    }

    function proceedToCheckout() {
      window.location.href = `checkout.html?price=${price}&title=${encodeURIComponent(prodTitle)}&img=${encodeURIComponent(prodImg)}`;
    }
  </script>"""

j_cart = re.sub(r'<script>\s*function getQueryParam\(name\).*?</script>', cart_js_jbl, j_cart, flags=re.DOTALL)
j_cart = re.sub(r'onclick="window\.location\.href\s*=\s*`checkout\.html\?price=\$\{price\}`"', 'onclick="proceedToCheckout()"', j_cart)

with open(jbl_cart, 'w', encoding='utf-8') as f:
    f.write(j_cart)

print("JBL Charge 6 index.html and cart.html updated successfully with 5 real colorways!")
