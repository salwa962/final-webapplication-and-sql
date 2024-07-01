from flask import Flask, render_template_string, request, send_file, redirect, url_for
import pyttsx3
import os
app = Flask(__name__)
engine = pyttsx3.init()


ebooks = {
    "1": """The Little Star's Journey
    In a small village in the African savannah, there was a young boy named Kofi who loved to stargaze. Every night, he would lay on the grass and look up at the twinkling stars, dreaming of adventures beyond his village. One night, a little star fell from the sky, landing softly beside Kofi.
    The star was scared and lost, far from its home in the sky. Kofi, determined to help, decided to embark on a journey to return the star to its place. With his trusty lantern and a heart full of courage, Kofi and the star set off on their adventure.
    They traveled through dense forests, crossed rivers, and climbed mountains, meeting various animals who offered their help along the way. Each challenge they faced only strengthened their bond and resolve. Finally, after a long journey, they reached the highest peak where the star could return to the sky.
    With a final hug, Kofi let go of the star, watching it rise and shine brightly among its friends. The star promised to watch over Kofi and his village, reminding him that even the smallest acts of kindness can light up the darkest nights.""",

    "2": """The Rainbow Garden
    In a colorful village nestled in the hills, a young girl named Amara loved to plant flowers. Her garden was her sanctuary, filled with blooms of every color. But one year, a severe drought hit the village, and Amara’s garden began to wither.
    Determined not to lose hope, Amara sought the help of the village elders, who told her of a magical spring hidden deep in the forest that could bring life back to her garden. With her watering can and a heart full of determination, Amara ventured into the forest.
    Along the way, she met animals in need of help—a thirsty deer, a lost bird, and a tired rabbit. Amara shared her water and food with them, despite her own need to save her garden. In return, the animals guided her to the magical spring.
    Amara filled her watering can with the spring’s water and hurried back to her village. As she sprinkled the water over her garden, the flowers began to bloom again, even more vibrant than before. The villagers, inspired by Amara’s kindness and perseverance, joined her in creating a community garden, ensuring that everyone would have a place to find beauty and hope.""",

    "3": """The Tale of the Brave Little Kite
    In a bustling seaside town, a young boy named Aiko loved to fly kites. His favorite was a colorful dragon kite that soared high above the beach. One windy day, Aiko’s kite flew so high that it got tangled in a tall tree on a nearby island.
    Determined to rescue his kite, Aiko built a small raft and set sail to the island. The journey was tough, with strong waves and winds challenging his every move. But Aiko’s love for his kite kept him going.
    Upon reaching the island, Aiko faced another challenge—the tree was guarded by a family of mischievous monkeys. Instead of shooing them away, Aiko shared his snacks with the monkeys and played with them. Grateful for his kindness, the monkeys helped Aiko retrieve his kite.
    With his kite back in hand, Aiko returned to the town, greeted by cheers from the villagers. His bravery and kindness had not only saved his kite but also taught everyone the importance of compassion and determination. From that day on, Aiko’s dragon kite became a symbol of hope, flying high above the beach, reminding everyone of the power of kindness and courage.""",

    "4": """From Home to Hope
    The sun rose over Gaza, casting its golden rays on the shattered remains of Shuja'iyya. Youssef, twelve years old, watched as his family prepared to leave their home for the last time. Their once vibrant neighborhood was now a landscape of ruins, with the echoes of laughter replaced by the distant sounds of conflict.
    Youssef’s father, Ahmed, packed what little they could salvage into a few bags. His mother, Fatima, held his younger sister, Leila, close, trying to mask her fear with a brave smile. “We need to move quickly,” Ahmed urged, his voice tight with urgency and sorrow.
    They joined a stream of families heading towards the temporary shelters set up on the outskirts of the city. The journey was perilous, with the constant threat of airstrikes hanging over them. But driven by hope for safety, they pressed on.
    After hours of walking, they reached a sprawling camp filled with rows of tents. Aid workers distributed food, water, and blankets. Youssef’s family was assigned a small, olive-green tent at the edge of the camp. The tent, with its thin canvas walls, offered little comfort, but it was their new home.
    Days turned into weeks. Ahmed found work with the aid organizations, and Fatima joined other women in cooking communal meals. Youssef and Leila made friends among the other displaced children, playing games and attending makeshift classes organized by volunteers. In these moments, they found brief escapes from the harsh realities around them.
    One evening, Youssef sat outside the tent with his father. “Do you think we’ll ever go back home?” he asked.
    Ahmed placed a reassuring hand on his son’s shoulder. “One day, Inshallah. Home is not just a building, Youssef. It’s our family, our memories, and our dreams. As long as we have each other, we have hope.”
    Youssef nodded, comforted by his father’s words. He looked around the camp and saw families sharing meals, children laughing, and neighbors supporting each other. In the face of adversity, the community had come together, their resilience shining through the darkness.
    That night, as he lay on the thin mat inside the tent, Youssef closed his eyes and imagined a future where they would return to Shuja'iyya, rebuild their home, and restore their lives. He held onto that vision tightly, knowing that hope was their greatest strength.
    And so, amidst the tents and turmoil, Youssef’s story of resilience and hope continued to unfold, proving that even in the darkest times, the light of human spirit could never be extinguished.""",

    "5": """A New Dawn in Aleppo
    The morning light barely pierced through the smoky haze over Aleppo. Thirteen-year-old Noor stood at the window of her family's battered apartment, surveying the rubble-strewn streets of her once-vibrant city. Inside, her father, Khaled, boiled water, while her mother, Layla, patched Noor's only remaining dress. Her younger brother, Sami, played with a makeshift toy car made from discarded scraps.
    "Stay close, Noor. We may need to leave quickly," Khaled warned. The family lived in constant readiness, always prepared to flee at a moment's notice due to the relentless bombardments. Noor missed school and the normalcy it brought. Now, her education came from stories and lessons shared by her father, a former teacher.
    That day, an unusual calm settled over the city as evening approached. Seizing the opportunity, the family ventured to a nearby aid distribution point. The journey was perilous, every step shadowed by the threat of snipers and sudden attacks. At the center, they received bread, water, and a small first aid kit—barely enough to last a few days, but a lifeline nonetheless.
    Returning home, Noor noticed the resilience in the faces of those around her. Despite the hardships, a quiet determination bound them together. Back in their apartment, the family shared a simple meal in silence. After dinner, Khaled told a story of a mythical bird rising from the ashes, symbolizing hope and renewal.
    "We will rise again, my dear," Khaled reassured Noor and Sami. "No matter how hard things get, we will rebuild. We will create a new life from the ruins of the old."
    That night, the family huddled together for warmth. Noor lay awake, her father's words echoing in her mind. Despite the destruction, she felt a flicker of hope. She closed her eyes, dreaming of a future where Aleppo would once again be a city of light and laughter.
    In the war-torn city, Noor found strength in her family and hope in the promise of a new dawn. As the first light of morning touched the horizon, she knew that no matter the challenges ahead, they would face them together.""",

    "6": """Whispers of Change
    In the streets of Khartoum, Sudan, whispers of change stirred the air. Fatima, a university student, felt the pulse of her nation quicken as protests swelled against decades of oppression. With courage in her heart, she joined the swelling crowds, raising her voice for justice and freedom.
    As days stretched into weeks, the protests grew, met with violent resistance from the ruling regime. Tear gas and bullets filled the air, but Fatima and her comrades stood firm, their resolve unyielding. Despite the danger, hope burned bright in their eyes, fueling their fight for a better Sudan.
    International support bolstered their cause, shining a spotlight on their struggle. And then, a breakthrough: the dictator fell, toppled by the collective will of the people. In the streets, jubilation erupted as Sudan embraced a new dawn of democracy.
    But amidst the celebrations, Fatima knew their journey was far from over. The road to true freedom would be fraught with challenges, but with unity and determination, she believed in a Sudan where justice and equality reigned.
    In the heart of Khartoum, where whispers of change had sparked a revolution, Fatima stood tall, ready to build a brighter future for her homeland.""",

    "7": """The Lantern of Hope
    The bustling markets of Damascus, Syria, were filled with the aroma of spices and the chatter of merchants. Amidst the crowd, twelve-year-old Zainab clung to her mother's hand, her eyes wide with curiosity. Life had always been vibrant in their city, but the shadows of war had begun to creep in, casting a pall over their daily lives.
    One evening, as they returned home, Zainab's father, Omar, brought out an old lantern from his shop. "This lantern has guided our family for generations," he explained. "It symbolizes hope and light in the darkest times."
    As the conflict intensified, the family's life was upended. Their home was damaged, and they were forced to flee to a refugee camp. Amidst the uncertainty and fear, the lantern became a beacon of hope for Zainab. Every night, Omar would light it, sharing stories of resilience and courage.
    In the camp, Zainab found solace in helping others. She volunteered at the makeshift school, teaching younger children and organizing games. Her spirit of kindness and hope inspired those around her, bringing a sense of community to the displaced families.
    Months passed, and news of a possible return home spread through the camp. Though their city lay in ruins, the hope of rebuilding kept their spirits alive. Zainab's family, clutching the lantern, joined the caravan of refugees returning to Damascus.
    As they walked through the ravaged streets, the lantern's light flickered but did not extinguish. It guided them back to their neighborhood, where they began the arduous task of rebuilding their home and lives.
    The Lantern of Hope became a symbol in their community, a reminder that even in the darkest times, hope and resilience could light the way forward. And so, Zainab's story of courage and kindness continued, illuminating the path to a brighter future for all.""",

    "8": """Echoes of Sakura
    In a quaint village in Japan, nestled among cherry blossom trees, lived a girl named Hana. The arrival of spring always brought a sea of pink petals, creating a magical landscape that Hana adored. She would spend hours beneath the sakura, dreaming of adventures and writing stories in her journal.
    One spring, an unexpected storm ravaged the village, and many of the beloved cherry trees were damaged. The villagers were heartbroken, fearing they would never see the beautiful blossoms again. Determined to restore the beauty of her village, Hana decided to take action.
    She gathered seeds from the remaining cherry trees and, with the help of her family and friends, began planting new ones. Despite the challenges, Hana's unwavering spirit inspired everyone around her. Together, they nurtured the young trees, protecting them from further harm.
    As the years passed, the village slowly regained its charm. The cherry blossoms returned, even more vibrant than before, symbolizing the resilience and unity of the community. Hana's stories, filled with hope and perseverance, spread beyond the village, touching the hearts of many.
    Each spring, as the sakura bloomed, the village celebrated Hanami, honoring Hana's dedication and the enduring spirit of their community. The echoes of her efforts lived on, reminding everyone that even in the face of adversity, hope and determination could bring about a beautiful transformation.""",
}

summaries = {
    "1": "A young boy named Kofi embarks on an adventure to return a fallen star to the sky, learning about courage and kindness along the way.",
    "2": "Amara, a young girl, saves her withering garden during a drought by seeking a magical spring, and in the process, creates a community garden with her village.",
    "3": "Aiko, a boy who loves flying kites, rescues his favorite kite from an island with the help of some monkeys, teaching his village about compassion and determination.",
    "4": "Youssef's family flees their war-torn home in Gaza, finding hope and resilience in a refugee camp as they dream of returning and rebuilding.",
    "5": "Noor's family navigates the perils of war in Aleppo, finding strength in their unity and hope for a brighter future amidst the ruins.",
    "6": "Fatima, a university student in Khartoum, joins the protests for freedom, witnessing the fall of a dictator and the dawn of a new democratic era in Sudan.",
    "7": "Zainab's family finds hope in a lantern as they navigate the challenges of war and displacement, inspiring their community with resilience and kindness.",
    "8": "Hana, a girl from a Japanese village, helps replant cherry blossom trees after a storm, restoring the beauty of her village and spreading a message of hope and unity.",
}


comments = {story_id: [] for story_id in ebooks.keys()}

@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Storyline Central</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                background-color: #f5efef;
                background-image: url('{{ url_for('static', filename='images/play.gif') }}');
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                font-family: Arial, sans-serif;
                color: #0c0c0c;
                padding: 20px;
            }
            .hidden-content {
                display: none;
            }
            .comment-section {
                max-width: 300px;
                margin: 10px auto;
                padding: 10px;
                background-color: beige;
                border-radius: 5px;
                font-size: 0.9em;
            }
            .comment {
                margin-bottom: 5px;
                padding: 5px;
                background-color: white;
                border-radius: 3px;
                border: 1px solid #ccc;
            }
            .comment p {
                margin: 0;
                font-size: 0.9em;
            }
            .comment-form {
                margin-top: 5px;
            }
            .comment-form textarea {
                width: 100%;
                max-width: 100%;
                font-size: 0.9em;
            }
            .toggle-comment-form, .comment-form button[type="submit"] {
                font-size: 0.9em;
                padding: 5px 10px;
            }
            .delete-form button {
                font-size: 0.8em;
                padding: 2px 5px;
            }
            .story-container {
                display: flex;
                align-items: center;
                margin-bottom: 10px;
            }
            .story-title {
                font-size: 14px;
                font-weight: normal;
                color: white;
            }
            .story-actions {
                margin-left: 20px;
            }
            .topnav {
                background-color: beige;
                overflow: hidden;
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                z-index: 1000;
            }
            .topnav a {
                float: left;
                color: brown;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 17px;
            }
            .topnav a:hover {
                background-color: #ddd;
                color: black;
            }
            .topnav a.active {
                background-color: #04AA6D;
                color: white;
            }
            .topnav input[type=text] {
                float: right;
                padding: 6px;
                border: none;
                margin-top: 8px;
                margin-right: 16px;
                font-size: 17px;
            }
            @media screen and (max-width: 600px) {
                .topnav a, .topnav input[type=text] {
                    float: none;
                    display: block;
                    text-align: left;
                    width: 100%;
                    margin: 0;
                    padding: 14px;
                }
                .topnav input[type=text] {
                    border: 1px solid #ccc;
                }
            }
            body {
                padding-top: 60px;
            }
        </style>
    </head>
    <body>
    
      <div class="topnav">
    <a href="#" class="active" onclick="showContent('home')">Home</a>
    <a href="#" onclick="showContent('about')">About</a>
    <a href="#" onclick="showContent('contact')">Contact</a>
    <input type="text" id="searchInput" placeholder="Search.." onkeyup="searchStories()">
</div>

<div id="home" class="content-section">
    <!-- Your existing story list goes here -->
    <div id="storyList">
        {% for id, title in ebooks.items() %}
        <!-- ... (keep your existing story list HTML) ... -->
        {% endfor %}
    </div>
</div>

<div id="about" class="content-section" style="display: none;">
    <h2>About Us</h2>
    <p>Welcome to Storyline Central, where we share inspiring stories of strength and resilience from around the world.</p>
</div>

<div id="contact" class="content-section" style="display: none;">
    <h2>Contact Us</h2>
    <p>You can reach us at contact@storylinecentral.com</p>
</div>

                                  
        <div style="position: fixed; top: 0; left: 0; padding: 10px;">
            <a href="https://www.audible.com/ep/2book?twobooketest=true">
                <img src="{{ url_for('static', filename='images/bird.jpg') }}" alt="bird" style="height: 40px; width: 100px;">
            </a>
        </div>
        <h1 style="margin-left: 120px; font-size: 2em; color: brown;">
            <a href="https://www.audible.com/ep/2book?twobooketest=true" style="text-decoration: none; color: inherit;">Stories of Strength</a>
        </h1>
        <div style="margin-bottom: 20px;" id="storyList">
            {% for id, title in ebooks.items() %}
            <div class="story-container" id="story-container{{ id }}">
                <a href="#" onclick="downloadStory('{{ id }}');" style="margin-right: 10px;">
                    <img src="{{ url_for('static', filename='images/my.jpg') }}" alt="eBook" style="height: 60px; width: 60px;">
                </a>
                <span class="story-title">{{ title.split('\\n')[0] }}</span>
            </div>
            <div id="story-content{{ id }}" class="story-content hidden-content">
                <p style="color: white;">{{ title }}</p>
            </div>
            <button onclick="toggleText('summary{{ id }}');" style="background-color: green; color: white;">READ</button>
            <p id="summary{{ id }}" style="display:none; color: white;">{{ summaries[id] }}</p>
            <audio id="audio-story{{ id }}" controls></audio>
            <button onclick="playAudio('{{ id }}')" style="background-color: blue; color: white;">LISTEN</button>
            <div style="margin-top: 10px;">
                <a href="#" onclick="shareOnFacebook('{{ id }}');"><img src="{{ url_for('static', filename='images/face.jpg') }}" alt="Share on Facebook" style="height: 30px; width: 30px;"></a>
                <a href="#" onclick="shareOnTwitter('{{ id }}');"><img src="{{ url_for('static', filename='images/twitter.jpg') }}" alt="Share on Twitter" style="height: 30px; width: 30px;"></a>
            </div>
            <div class="comment-section">
                {% for comment in comments[id] %}
                <div class="comment">
                    <p>{{ comment }}</p>
                    <form class="delete-form" method="POST" action="{{ url_for('delete_comment', story_id=id, comment_index=loop.index) }}">
                        <button type="submit" style="background-color: red; color: white;">Delete</button>
                    </form>
                </div>
                {% endfor %}
                <form class="comment-form" method="POST" action="{{ url_for('add_comment', story_id=id) }}">
                    <textarea name="comment" rows="2"></textarea>
                    <br>
                    <button type="submit" style="background-color: brown; color: white;">WRITE REVIEW</button>
                </form>
            </div>
            {% endfor %}
        </div>
        <script>
       function searchStories() {
    const input = document.getElementById('searchInput').value.trim().toLowerCase();
    const stories = document.getElementsByClassName('story-container');
    
    for (let i = 0; i < stories.length; i++) {
        const title = stories[i].getElementsByClassName('story-title')[0].innerText.toLowerCase();
        const contentId = 'story-content' + stories[i].id.replace('story-container', '');
        const content = document.getElementById(contentId);
        
        if (input === "") {
            // If search input is empty, show all stories and hide all content
            stories[i].style.display = '';
            content.style.display = 'none';
        } else {
            // Check if the title contains the input text
            if (title.includes(input)) {
                stories[i].style.display = '';
                content.style.display = 'block';
            } else {
                stories[i].style.display = 'none';
                content.style.display = 'none';
            }
        }
    }
}




            function toggleText(summaryId) {
                const summary = document.getElementById(summaryId);
                summary.style.display = summary.style.display === 'none' ? 'block' : 'none';
            }

            function playAudio(storyId) {
                fetch('/play/' + storyId)
                    .then(response => response.blob())
                    .then(audioBlob => {
                        const audioElement = document.getElementById('audio-story' + storyId);
                        audioElement.src = URL.createObjectURL(audioBlob);
                        audioElement.play();
                    });
            }

            function shareOnFacebook(storyId) {
                const storySummary = document.getElementById('summary' + storyId).innerText;
                const url = 'https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(window.location.href) + '&quote=' + encodeURIComponent(storySummary);
                window.open(url, '_blank');
            }

            function shareOnTwitter(storyId) {
                const storySummary = document.getElementById('summary' + storyId).innerText;
                const url = 'https://twitter.com/intent/tweet?text=' + encodeURIComponent(storySummary) + '&url=' + encodeURIComponent(window.location.href);
                window.open(url, '_blank');
            }
                                  function showContent(contentId) {
    // Hide all content sections
    var contentSections = document.getElementsByClassName('content-section');
    for (var i = 0; i < contentSections.length; i++) {
        contentSections[i].style.display = 'none';
    }
    
    // Show the selected content section
    document.getElementById(contentId).style.display = 'block';
    
    // Update active class in navigation
    var navLinks = document.getElementsByClassName('topnav')[0].getElementsByTagName('a');
    for (var i = 0; i < navLinks.length; i++) {
        navLinks[i].classList.remove('active');
        if (navLinks[i].getAttribute('onclick').includes(contentId)) {
            navLinks[i].classList.add('active');
        }
    }
}

            function downloadStory(storyId) {
                window.location.href = '/download/' + storyId;
            }
        </script>
    </body>
    </html>
    """, ebooks=ebooks, summaries=summaries, comments=comments)

# Define the route to download a story
@app.route('/download/<story_id>')
def download_story(story_id):
    story_content = ebooks.get(story_id)
    if story_content:
        filename = f"story_{story_id}.txt"
        with open(filename, 'w') as file:
            file.write(story_content)
        return send_file(filename, as_attachment=True)
    return "Story not found", 404

# Define the route to play a story using text-to-speech
@app.route('/play/<story_id>')
def play_story(story_id):
    story_content = ebooks.get(story_id)
    if story_content:
        engine.save_to_file(story_content, 'story.mp3')
        engine.runAndWait()
        return send_file('story.mp3', mimetype='audio/mp3')
    return "Story not found", 404

# Define the route to add a comment
@app.route('/add_comment/<story_id>', methods=['POST'])
def add_comment(story_id):
    comment = request.form.get('comment')
    if comment:
        comments[story_id].append(comment)
    return redirect(url_for('index'))

# Define the route to delete a comment
@app.route('/delete_comment/<story_id>/<int:comment_index>', methods=['POST'])
def delete_comment(story_id, comment_index):
    if 0 <= comment_index < len(comments[story_id]):
        comments[story_id].pop(comment_index)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)