from django.shortcuts import render

# Create your views here.

articles = [
        {
            "title":"48MP Fusion Main camera with variable aperture",

            "des":"Apple’s iPhone 18 Pro Max is a premium flagship smartphone designed for users who want powerful performance, advanced photography, a stunning display, and a refined overall experience. It combines a sophisticated design with high-end hardware and Apple’s latest-generation technology, making it suitable for everyday use, entertainment, photography, gaming, and professional tasks."

            " The iPhone 18 Pro Max features a large, immersive display that delivers vibrant colors, deep contrast, sharp details, and smooth animations. Whether you are watching movies, browsing social media, editing photos, or playing games, the expansive screen provides an engaging viewing experience. The display is designed to remain bright and readable in different lighting conditions while maintaining excellent visual quality."

            "At the heart of the iPhone 18 Pro Max is a powerful next-generation Apple chip built to handle demanding applications and intensive workloads. It provides fast performance, efficient multitasking, smooth gaming, and responsive app launches. Combined with optimized iOS software, the phone is designed to deliver a fluid experience even when multiple applications and demanding processes are running at the same time."

            "Photography is another major highlight. The iPhone 18 Pro Max offers an advanced multi-camera system designed to capture detailed photos and high-quality videos in a wide range of lighting conditions. Its cameras are suitable for portraits, landscapes, close-up photography, night scenes, and everyday moments. Computational photography and intelligent image processing help improve details, colors, exposure, and overall image quality."

            "For video creators, the iPhone 18 Pro Max provides powerful recording capabilities with smooth stabilization and detailed footage. It can be used for creating social-media content, travel videos, short films, product videos, and professional-looking clips without requiring a dedicated camera for many situations."

            "The phone also focuses heavily on battery efficiency. Its large battery and power-efficient hardware are designed to provide long-lasting usage throughout the day. Whether you are streaming content, browsing the internet, using navigation, taking photos, or communicating with friends and family, the device is built to support extended everyday use."

            "The premium construction gives the iPhone 18 Pro Max a sophisticated appearance while providing a durable feel in the hand. Apple’s attention to materials, finishing, and details gives the device a polished flagship identity. The phone also includes modern connectivity features, allowing users to take advantage of fast wireless communication and reliable connections with compatible devices and accessories."

            "With the latest version of iOS, the iPhone 18 Pro Max provides access to Apple’s ecosystem of applications and services. Features such as privacy controls, security protections, cloud synchronization, and seamless integration with other Apple devices make it convenient for users who already use products such as Mac, iPad, Apple Watch, or AirPods."

            "Overall, the iPhone 18 Pro Max is designed as an all-round premium smartphone that combines powerful performance, advanced cameras, a large high-quality display, strong battery life, modern connectivity, and a polished software experience. It is aimed at users who want a flagship device capable of handling everything from everyday communication and entertainment to photography, gaming, content creation, and demanding productivity tasks.",

            "name":"John Ternus",
            "date":"Sep 15 2026",
            "up_time":"3 day's ago",
            "image":"assets/iphone.png",
            "user_img":"assets/user1.png",

        },
        {
            "title":"Easy-to-grow fruit plants for first-time gardeners",

            "des":"Growing fruit plants at home can be a rewarding and enjoyable experience, especially for first-time gardeners. You do not need a large garden or years of gardening experience to start. Many fruit plants are relatively easy to grow and can thrive in pots, balconies, terraces, backyards, or small garden spaces when they receive proper sunlight, water, and care. Choosing beginner-friendly plants is a great way to gain confidence while enjoying fresh fruit grown at home."

            "One of the easiest fruit plants for beginners is the strawberry. Strawberries can grow well in containers, hanging baskets, and small garden beds. They generally need several hours of sunlight and well-draining soil. With regular watering and occasional feeding, strawberry plants can produce attractive flowers followed by sweet, colorful fruits. Their compact size also makes them suitable for people with limited space."

            "Lemon plants are another popular choice for home gardeners. Dwarf lemon varieties can be grown successfully in large containers and can provide fragrant flowers and fresh lemons. Lemon plants prefer plenty of sunlight and need soil that drains well. Regular watering is important, but the roots should not remain in standing water. With proper care, a healthy lemon plant can remain productive for years."

            "Guava is also suitable for gardeners living in warm climates. Guava plants are generally vigorous and can grow into productive fruit trees when provided with adequate sunlight, water, and nutrients. Dwarf or container-friendly varieties can be particularly useful for smaller spaces. Their attractive foliage and fragrant fruit make them a useful addition to a home garden."

            "For gardeners with warmer conditions, papaya can be an interesting option. Papaya plants grow relatively quickly compared with many traditional fruit trees and can produce fruit when given suitable growing conditions. They require sunlight, regular moisture, and sufficient space for their roots and leaves. Because they can become tall, gardeners should consider their available space before planting."

            "Fig plants are another option for beginners, particularly when suitable varieties are selected. Figs can be grown in containers and generally prefer sunny locations with good drainage. They can tolerate periods of dry conditions once established, although consistent care helps support healthy growth and fruit production."

            "Pomegranate is also worth considering for a home garden. It can grow in containers or directly in the ground and generally prefers warm, sunny conditions. Once established, pomegranate plants can be relatively resilient and require less intensive care than some other fruit trees."

            "When starting a fruit garden, beginners should pay attention to a few basic requirements. Select healthy plants from a reliable nursery, choose a container large enough for the plant, use nutrient-rich and well-draining soil, and make sure the plant receives the amount of sunlight it needs. Avoid overwatering, as excessive moisture can damage roots. Pruning, fertilizing, and checking regularly for pests can also help maintain healthy growth."

            "The best fruit plant ultimately depends on the local climate, available space, sunlight, and the gardener's ability to provide regular care. Starting with one or two easy-to-manage varieties can make the learning process simple and enjoyable. With patience and consistent attention, first-time gardeners can gradually create a productive home fruit garden and enjoy the satisfaction of harvesting fresh fruit they have grown themselves.",

            "name":"NewsPoint",
            "date":"Jun 8 2022",
            "up_time":"2 min ago",
            "image":"assets/strawbery.png",
            "user_img":"assets/user2.png"
        },
        {
            "title":"SpaceX Expands NASA Crew Mission Deal to $5.92 Billion",

            "des":"SpaceX has expanded its partnership with NASA through a major increase in the value of its crew transportation agreement, bringing the total deal to approximately $5.92 billion. The agreement supports NASA’s efforts to transport astronauts safely between Earth and the International Space Station (ISS) using SpaceX’s Crew Dragon spacecraft and Falcon 9 rockets."

            "The partnership began under NASA’s Commercial Crew Program, which was created to encourage private companies to develop reliable spacecraft capable of carrying astronauts into orbit. SpaceX became one of NASA’s key commercial crew providers, helping restore regular crew transportation from the United States to the ISS."

            "Under the expanded agreement, SpaceX will continue providing crew transportation services, including spacecraft preparation, rocket launches, astronaut transportation, and recovery operations. The missions are designed to support long-duration stays aboard the International Space Station and maintain a continuous human presence in low Earth orbit."

            "Crew Dragon has become an important part of NASA’s modern human-spaceflight program. The spacecraft is designed to carry astronauts safely to orbit, dock with the ISS, and return them to Earth. Falcon 9 rockets provide the launch capability, with reusable rocket technology helping support repeated missions."

            "The expanded contract also reflects NASA’s broader strategy of working with commercial space companies for human spaceflight. Instead of relying entirely on government-owned transportation systems, NASA can purchase transportation services from private providers while concentrating its resources on exploration missions farther from Earth."

            "SpaceX’s crew missions are also connected to NASA’s longer-term plans for lunar exploration and future human spaceflight. Experience gained through commercial crew operations, spacecraft development, astronaut training, and mission management contributes to the growing capabilities of the commercial space industry."

            "The $5.92 billion figure represents the overall value of the NASA agreement and its modifications rather than a single launch. The partnership demonstrates the increasingly important role of commercial companies in NASA’s human-spaceflight operations and the continuing development of privately operated space transportation systems.",

            "name":"GK Today",
            "date":"Sep 15 2026",
            "up_time":"2 day's ago",
            "image":"assets/nasa.png",
            "user_img":"assets/user3.png",
        },
        {
            "title":"Largest Software Training Organization",

            "des":"QSpiders Bangalore is a well-known software training and placement-focused institute that provides technical education for students, fresh graduates, and aspiring IT professionals. The institute is particularly known for offering training programs in software development, testing, programming, databases, and other technologies commonly used in the IT industry."

            "QSpiders focuses on helping learners build practical technical skills alongside their academic knowledge. Its training programs generally cover important areas such as Java, Python, SQL, web technologies, software testing, automation testing, and other programming and development concepts. The curriculum is designed to help students understand both fundamental concepts and practical applications through classes, exercises, assignments, and project-based learning."

            "One of the important features of QSpiders is its emphasis on software testing and development-related career preparation. Students interested in manual testing can learn concepts such as software testing fundamentals, test scenarios, test cases, functional testing, integration testing, system testing, regression testing, and defect reporting. Depending on the selected course, students can also learn automation-related technologies and tools used in the software industry."

            "For students interested in development, training may include programming languages and technologies such as Java, Python, SQL, HTML, CSS, JavaScript, and other web-development concepts. Learning these technologies can help students develop a stronger foundation for entry-level software development and IT roles."

            "QSpiders Bangalore also places importance on interview and placement preparation. Students can practice aptitude, technical questions, coding problems, communication skills, resume preparation, and interview techniques. Such preparation can help candidates become more comfortable with technical interviews and recruitment processes. Placement assistance may also provide opportunities to participate in recruitment drives conducted by companies looking for entry-level candidates."

            "The learning environment at QSpiders is structured around regular classes and practice. Students are generally encouraged to solve programming exercises, participate in discussions, complete assignments, and strengthen their understanding through repeated practice. For beginners, this type of structured learning can be useful because it provides a learning path from basic concepts toward more advanced technical topics."

            "Another important aspect is the community of students preparing for IT careers. Studying alongside other learners can provide opportunities for discussion, peer learning, and sharing information about interview experiences and technical preparation. Students can also use their training period to work on personal projects and build a portfolio that demonstrates their practical skills."

            "QSpiders Bangalore is located in Bengaluru, one of India's major technology and IT hubs. Bengaluru has a large ecosystem of software companies, startups, technology services firms, and multinational organizations. This makes the city an important location for students preparing for careers in the software industry."

            "For a student or fresher, QSpiders can be considered as one part of a broader career-preparation strategy. Training can provide structured technical learning, but students can strengthen their profile further by practicing coding independently, building real-world projects, improving communication skills, learning Git and GitHub, preparing a strong resume, and developing problem-solving abilities."

            "Overall, QSpiders Bangalore provides a training-oriented environment for people looking to develop software and testing skills and prepare for entry-level IT opportunities. Its combination of technical classes, practical exercises, interview preparation, and placement-oriented activities makes it relevant to students and fresh graduates who are working toward starting their careers in the software industry.",

            "name":"Prajwal",
            "date":"Sep 15 2026",
            "up_time":"56 min ago",
            "image":"assets/qspider.png",
            "user_img":"assets/user4.png",
        },
        {
            "title":"What is the Scientific Name of Rose?",

            "des":"The scientific name commonly used for the rose plant is Rosa, which is the genus belonging to the family Rosaceae. Roses are flowering plants known for their beautiful flowers, pleasant fragrance, and wide variety of colors, including red, pink, white, yellow, and orange."

            "It is important to note that there is no single scientific name for every rose because roses include many different species and cultivated varieties. For example, the scientific name of the China rose is Rosa chinensis, while the dog rose is scientifically known as Rosa canina. The widely cultivated Damask rose is commonly identified as Rosa × damascena."

            "Roses are native to various regions of the Northern Hemisphere and are now cultivated worldwide as ornamental plants. They can grow as shrubs, climbers, or compact garden plants depending on the species and variety. Roses are commonly grown in gardens, parks, landscapes, and containers."

            "Apart from their ornamental value, roses have several other uses. Rose petals are used in perfumes, cosmetics, traditional preparations, and food products such as rose water and certain sweets."

            "In short, Rosa is the scientific genus name for roses, while individual rose species have their own scientific names.",
            "name":"Jagran Josh",
            "date":"Oct 12 2026",
            "up_time":"7 day's ago",
            "image":"assets/rose.png",
            "user_img":"assets/user5.png",
        },
        {
            "title":"Want Korean glass skin? 5 habits make all the difference",

            "des":"Korean glass skin refers to skin that looks hydrated, smooth, healthy, and naturally radiant. While skincare products can help, achieving this appearance is less about having a complicated routine and more about following simple habits consistently"

            "1. Keep your skin hydrated: Hydration helps maintain a healthy-looking skin barrier and can make the skin appear smoother and more plump. Drink enough water throughout the day and use a moisturizer suited to your skin type."

            "2. Cleanse gently: Washing your face helps remove sweat, dirt, oil, and makeup. Choose a gentle cleanser and avoid scrubbing aggressively, as excessive cleansing can leave the skin feeling dry or irritated."

            "3. Never skip sunscreen: Daily sun protection is one of the most important skincare habits. Use a broad-spectrum sunscreen during the daytime and reapply when appropriate, especially when spending extended periods outdoors."

            "4. Follow a simple routine: You do not need dozens of products. A basic routine can include cleansing, moisturizing, and sunscreen, with optional products such as a gentle serum depending on your skin’s needs. Introduce new products gradually."

            "5. Prioritize healthy lifestyle habits: Adequate sleep, balanced nutrition, regular physical activity, and stress management can contribute to overall skin health. Avoiding smoking and limiting excessive alcohol consumption can also support healthier-looking skin."

            "Glass skin is not about achieving perfectly poreless or flawless skin. Natural pores, texture, and occasional blemishes are normal. The goal should be healthy, comfortable, well-hydrated skin rather than perfection. Consistency, patience, and choosing products that suit your individual skin type are more important than following every skincare trend.",

            "name":"Time Of India",
            "date":"Aug 05 2025",
            "up_time":"3 min ago",
            "image":"assets/glassskin.png",
            "user_img":"assets/user6.png",
        },
    ]

def home(request):
    return render(request,"home.html",{"article":articles[0]})

def about(request):
    return render(request,"about.html")

def latest(request):
    return render(request,"latest.html",{"articles":articles})

def features(request):
    return render(request,"features.html",{"article":articles[0]})

def contactus(request):
    return render(request,"contactus.html")

def article_detail(request,id):
    return render(request,"features.html",{"article":articles[id]})

def footer(request):
    return render(request,'footer.html')