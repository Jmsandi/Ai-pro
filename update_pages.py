#!/usr/bin/env python3
"""
Bulk content updater for AI Professional College pages:
- about.html, contact.html, faq.html, register.html
- course.html, course2.html, course3.html
- team.html, blog.html, event.html
"""

import os, re

BASE = '/Users/jmsandi/Downloads/purdue-1.0.0'

# ─── SHARED FOOTER ─────────────────────────────────────────────────────────────
FOOTER = '''	<!-- START FOOTER -->
	<div class="footer section-padding">
		<div class="container">				
			<div class="row">					
				<div class="col-lg-3 col-sm-6 col-xs-12">
					<div class="single_footer">
						<a href="index.html"><img src="assets/images/pro%20images/logo.jpg" alt="AI Professional College"></a>         
						<p>AI Professional College — established to provide industry-focused career development programs. We build professionals with exceptional skills and ethical standards.</p>
					</div>
					<div class="foot_social">
						<ul>
							<li><a href="#" class="top_f_facebook"><i class="fa-brands fa-facebook"></i></a></li>
							<li><a href="#" class="top_f_twitter"><i class="fa-brands fa-x-twitter"></i></a></li>
							<li><a href="#" class="top_f_instagram"><i class="fa-brands fa-instagram"></i></a></li>
							<li><a href="#" class="top_f_linkedin"><i class="fa-brands fa-linkedin-in"></i></a></li>
						</ul>					
					</div>					
				</div><!-- END COL -->					
				<div class="col-lg-2 col-sm-6 col-xs-12">
					<div class="single_footer">
						<h4>Programs</h4>
						<ul>
							<li><a href="course2.html">BSc Computer Science</a></li>
							<li><a href="course2.html">BSc Accounting</a></li>
							<li><a href="course2.html">BSc Business Administration</a></li>
							<li><a href="course2.html">BSc Human Resource Mgt</a></li>
							<li><a href="course3.html">ACCA &amp; CIMA</a></li>
							<li><a href="course.html">Masters Programs</a></li>
						</ul>
					</div>
				</div><!-- END COL -->	
				<div class="col-lg-2 col-sm-6 col-xs-12">
					<div class="single_footer">
						<h4>Quick Links</h4>
						<ul>
							<li><a href="about.html">About Us</a></li>
							<li><a href="team.html">Faculty &amp; Staff</a></li>
							<li><a href="event.html">Events</a></li>
							<li><a href="faq.html">Admissions FAQ</a></li>
							<li><a href="blog.html">News</a></li>
							<li><a href="contact.html">Contact Us</a></li>
						</ul>
					</div>
				</div><!-- END COL -->	
				<div class="col-lg-3 col-sm-6 col-xs-12">
					<div class="single_footer">
						<h4>Contact Info</h4>
						<div class="sf_contact">
							<span class="ti-mobile"></span>
							<h3>Phone Number</h3>
							<p>+233 (0) 000 000 000</p>
						</div>
						<div class="sf_contact">
							<span class="ti-email"></span>
							<h3>Email Address</h3>
							<p>info@aiprofessionals.org</p>
						</div>
						<div class="sf_contact">
							<span class="ti-map"></span>
							<h3>Our Address</h3>
							<p>AI Professional College, Ghana</p>
						</div>
					</div>
				</div><!-- END COL -->	
				</div><!-- END ROW -->		
			<div class="row fc">
				<div class="col-lg-6 col-sm-6 col-xs-12">
					<div class="footer_copyright">
						<p>&copy; 2025 AI Professional College. All Rights Reserved. | <a href="https://www.aiprofessionals.org" class="text-dark" target="_blank">aiprofessionals.org</a></p>
					</div>
				</div>
				<div class="col-lg-6 col-sm-6 col-xs-12">
					<div class="footer_menu">
						<ul>
							<li><a href="#">Terms of use</a></li>
							<li><a href="#">Privacy Policy</a></li>
							<li><a href="#">Cookie Policy</a></li>
						</ul>
					</div>
				</div><!-- END COL -->
			</div>				
		</div><!-- END CONTAINER -->
	</div>
	<!-- END FOOTER -->'''

# ─── TOP CONTACT ─────────────────────────────────────────────────────────────
OLD_PHONE = '+ 485 7548 8546'
NEW_PHONE = '+233 (0) 000 000 000'
OLD_EMAIL = 'example@mail.com'
NEW_EMAIL = 'info@aiprofessionals.org'
OLD_HOURS = 'Mon to sat Open: 9am - 6pm'
NEW_HOURS = 'Mon – Fri: 8am – 5pm'
OLD_TEL = 'tel:+4857548854826'
NEW_TEL = 'tel:+233000000000'
OLD_MAILTO = 'mailto:example@gmail.com'
NEW_MAILTO = 'mailto:info@aiprofessionals.org'

# ─── FOOTER REPLACEMENT REGEX ─────────────────────────────────────────────────
FOOTER_PATTERN = re.compile(
    r'<!-- START FOOTER -->.*?<!-- END FOOTER -->',
    re.DOTALL
)

# ─── META/TITLE per-page ─────────────────────────────────────────────────────
PAGE_TITLES = {
    'about.html':       ('About Us | AI Professional College',       'Learn about AI Professional College — our mission, vision, and history since 2014.'),
    'course.html':      ('All Programs | AI Professional College',   'Explore all programs at AI Professional College — Professional, Degree, and Masters qualifications.'),
    'course2.html':     ('Degree Programs | AI Professional College','BSc degree programs in Computer Science, Accounting, Business Admin, HRM, Marketing, Public Health, and more.'),
    'course3.html':     ('Professional Programs | AI Professional College', 'Professional certifications: ACCA, CIMA, CAT/FIA, IT Certifications at AI Professional College.'),
    'single_course.html': ('BSc Computer Science | AI Professional College', 'BSc Computer Science program at AIPC — train in web design, cybersecurity, systems analysis, and more.'),
    'team.html':        ('Faculty & Staff | AI Professional College', 'Meet the experienced faculty and staff at AI Professional College.'),
    'team-details.html':('Faculty Detail | AI Professional College', 'Faculty member profile at AI Professional College.'),
    'blog.html':        ('News & Events | AI Professional College',  'Latest news, announcements, and events from AI Professional College.'),
    'blog_single.html': ('News Detail | AI Professional College',    'News article from AI Professional College.'),
    'event.html':       ('Campus Events | AI Professional College',  'Upcoming campus events, activities, and programmes at AI Professional College.'),
    'event_single.html':('Event Detail | AI Professional College',   'Event details from AI Professional College.'),
    'contact.html':     ('Contact Us | AI Professional College',     'Get in touch with AI Professional College. Find our address, phone, and email.'),
    'faq.html':         ('Admissions FAQ | AI Professional College', 'Frequently asked questions about admissions, entry requirements, and programmes at AI Professional College.'),
    'login.html':       ('Student Portal | AI Professional College', 'Login to the AI Professional College student portal.'),
    'register.html':    ('Apply Now | AI Professional College',      'Apply to AI Professional College. Start your journey to becoming a certified professional.'),
    'error.html':       ('Page Not Found | AI Professional College', '404 — Page not found at AI Professional College.'),
    'index2.html':      ('AI Professional College — Quality Higher Education', 'AI Professional College — Discover Purpose, Choose Hope, Lead Change.'),
}

# ─── SECTION TOP titles per page ──────────────────────────────────────────────
SECTION_TOPS = {
    'about.html':       ('About Us',            'Home', 'index.html', 'About'),
    'course.html':      ('Our Programs',        'Home', 'index.html', 'Programs'),
    'course2.html':     ('Degree Programs',     'Programs', 'course.html', 'Degree Programs'),
    'course3.html':     ('Professional Programs','Programs','course.html','Professional Programs'),
    'single_course.html':('BSc Computer Science','Programs','course.html','Computer Science'),
    'team.html':        ('Faculty &amp; Staff', 'Home', 'index.html', 'Faculty'),
    'team-details.html':('Faculty Detail',      'Faculty', 'team.html', 'Detail'),
    'blog.html':        ('News &amp; Events',   'Home', 'index.html', 'News'),
    'blog_single.html': ('News Detail',         'News', 'blog.html', 'Detail'),
    'event.html':       ('Campus Events',       'Home', 'index.html', 'Events'),
    'event_single.html':('Event Detail',        'Events','event.html','Detail'),
    'contact.html':     ('Contact Us',          'Home', 'index.html', 'Contact'),
    'faq.html':         ('Admissions FAQ',      'Home', 'index.html', 'Admissions FAQ'),
    'login.html':       ('Student Portal Login','Home', 'index.html', 'Login'),
    'register.html':    ('Apply Now',           'Home', 'index.html', 'Apply Now'),
    'error.html':       ('Page Not Found',      'Home', 'index.html', '404'),
}

def build_section_top(title, parent_label, parent_href, current):
    return f'''		<!-- START SECTION TOP -->
		<section class="section-top">
			<div class="container">
				<div class="col-lg-10 offset-lg-1 text-center">
					<div class="section-top-title wow fadeInDown" data-wow-duration="1s" data-wow-delay="0.2s" data-wow-offset="0">
						<h1>{title}</h1>
						<ul>
							<li><a href="{parent_href}">{parent_label}</a></li>
							<li> / {current}</li>
						</ul>
					</div><!-- //.HERO-TEXT -->
				</div><!-- END COL -->
			</div><!-- END CONTAINER -->
		</section>	
		<!-- END SECTION TOP -->'''

# ─── CONTENT BLOCKS per page ──────────────────────────────────────────────────

ABOUT_MAIN = '''	<!-- START ABOUT US -->
	<section class="ab_one section-padding">
		<div class="container">								
			<div class="row">								
				<div class="col-lg-6 col-sm-12 col-xs-12 wow fadeInLeft" data-wow-duration="1s" data-wow-delay="0.2s" data-wow-offset="0">
					<div class="ab_img">
						<img src="assets/images/pro%20images/P-1%20%281%29.jpeg" class="img-fluid about-img-fit" alt="AI Professional College">
						<div class="wc_year">
							<h3><span>Est.</span> <br />2014</h3>
						</div>
					</div>
				</div><!-- END COL -->				
				<div class="col-lg-6 col-sm-12 col-xs-12 wow fadeInRight" data-wow-duration="1s" data-wow-delay="0.1s" data-wow-offset="0">
					<div class="ab_content">
						<h2>Welcome to AI Professional College</h2>
						<p>Established in 2014, AI Professional College provides industry-focused career development programs designed for emerging economies. Our teaching staff are drawn from experienced professionals working in leading organisations across Ghana and beyond.</p>
					</div>
					<div class="abmv">
						<i class="fa-solid fa-graduation-cap"></i>
						<h4>Career-Focused Graduates</h4>
						<p>We develop graduates equipped with practical professional skills and ethical standards ready for immediate workplace impact.</p>
					</div>	
					<div class="abmv">
						<i class="fa-solid fa-scale-balanced"></i>
						<h4>Equal Opportunity Institution</h4>
						<p>We provide equal educational opportunities for all students, regardless of background. We do not discriminate and focus on pathways for career advancement.</p>
					</div>	
					<div class="cta_two">
						<a href="register.html" class="cta"><span>Apply Now</span>
						  <svg width="13px" height="10px" viewBox="0 0 13 10">
							<path d="M1,5 L11,5"></path>
							<polyline points="8 1 12 5 8 9"></polyline>
						  </svg>
						</a>
					</div>
				</div><!-- END COL -->								  
			</div><!-- END ROW -->
		</div><!-- END CONTAINER -->
	</section>
	<!-- END ABOUT US -->

	<!-- START VISION & MISSION -->
	<section class="marketing_content_area section-padding">
	   <div class="container">
			<div class="section-title">
				<h4>Our Vision &amp; Mission</h4>
				<h1>Our Community, Our College.</h1>
			</div>		
			<div class="row">								
				<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.1s" data-wow-offset="0">
					<div class="single_feature_one">
						<div class="sf_top">
							<i class="fa-solid fa-eye"></i>
							<h2><a href="#">Our <br />Vision</a></h2>
						</div>
						<p>To improve lives, strengthen communities and foster student excellence, educational attainment, economic growth, and cultural enrichment.</p>
						<a href="contact.html">Learn More <i class="fa-solid fa-arrow-right"></i></a>
					</div>					
				</div><!-- END COL -->								
				<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.2s" data-wow-offset="0">
					<div class="single_feature_one">
						<div class="sf_top">
							<i class="fa-solid fa-bullseye"></i>
							<h2><a href="#">Our <br />Mission</a></h2>
						</div>	
						<p>To provide degree, diploma, and certificate programs in partnership with businesses, industries, and community groups to promote societal development.</p>
						<a href="contact.html">Learn More <i class="fa-solid fa-arrow-right"></i></a>
					</div>					
				</div><!-- END COL -->								
				<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.3s" data-wow-offset="0">
					<div class="single_feature_one">
						<div class="sf_top">
							<i class="fa-solid fa-handshake"></i>
							<h2><a href="#">Community <br />Partners</a></h2>
						</div>	
						<p>We partner with businesses, industries, community groups, and educational institutions to promote societal development and career advancement.</p>
						<a href="contact.html">Learn More <i class="fa-solid fa-arrow-right"></i></a>
					</div>					
				</div><!-- END COL -->								
				<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.4s" data-wow-offset="0">
					<div class="single_feature_one">
						<div class="sf_top">
							<i class="fa-solid fa-flask"></i>
							<h2><a href="#">Practical <br />Education</a></h2>
						</div>	
						<p>Our programs are designed around industry demands and emerging economic trends. We focus on practical education that creates real career pathways.</p>
						<a href="course.html">Learn More <i class="fa-solid fa-arrow-right"></i></a>
					</div>					
				</div><!-- END COL -->								
				<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.5s" data-wow-offset="0">
					<div class="single_feature_one">
						<div class="sf_top">
							<i class="fa-solid fa-building-columns"></i>
							<h2><a href="#">Industry <br />Affiliations</a></h2>
						</div>		
						<p>We are professionally affiliated with international accounting bodies, finance institutions, and leading IT organisations, including ACCA, CIMA, and CAT/FIA.</p>
						<a href="course3.html">Learn More <i class="fa-solid fa-arrow-right"></i></a>
					</div>					
				</div><!-- END COL -->								
				<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.6s" data-wow-offset="0">
					<div class="single_feature_one">
						<div class="sf_top">
							<i class="fa-solid fa-earth-africa"></i>
							<h2><a href="#">Equal <br />Opportunity</a></h2>
						</div>		
						<p>AI Professional College provides equal educational opportunities. We do not discriminate and ensure every student has access to quality education.</p>
						<a href="about.html">Learn More <i class="fa-solid fa-arrow-right"></i></a>
					</div>					
				</div><!-- END COL -->
			</div><!-- END ROW -->
		</div><!-- END CONTAINER -->
	</section>
	<!-- END VISION & MISSION -->

	<!-- STATS COUNTER -->
	<section class="count_area counter_feature">
		<div class="container">
			<div class="row">
				<div class="col-lg-3 col-sm-6 col-xs-12">
					<div class="single-counter count_one">
						<span class="ti-folder sc_one"></span>
						<h2 class="counter-num">9</h2>
						<p>Degree Programs</p>
					</div>						
				</div>
				<div class="col-lg-3 col-sm-6 col-xs-12">
					<div class="single-counter count_two">
						<span class="ti-medall-alt sc_two"></span>
						<h2 class="counter-num">2014</h2>
						<p>Year Established</p>
					</div>
				</div><!-- END COL -->
				<div class="col-lg-3 col-sm-6 col-xs-12">
					<div class="single-counter count_three">
						<span class="ti-id-badge sc_three"></span>
						<h2 class="counter-num">2000</h2>
						<p>Students Enrolled</p>
					</div>
				</div><!-- END COL -->
				<div class="col-lg-3 col-sm-6 col-xs-12">
					<div class="single-counter count_four">
						<span class="ti-user sc_four"></span>
						<h2 class="counter-num">500</h2>
						<p>Graduates</p>
					</div>
				</div><!-- END COL -->					
			</div><!-- END ROW -->
		</div><!-- END CONTAINER -->		
	</section>
	<!-- END STATS COUNTER -->

	<!-- QUALITY OF EDUCATION -->
	<section class="ab_one section-padding">
		<div class="container">
			<div class="section-title">
				<h4>Quality of Education</h4>
				<h1>Specialised in Business Studies &amp; Information Technology.</h1>
			</div>
			<div class="row">
				<div class="col-lg-6 col-sm-12 col-xs-12 wow fadeInLeft" data-wow-duration="1s" data-wow-delay="0.2s" data-wow-offset="0">
					<div class="ab_content">
						<h2>A Private Higher Education Institution</h2>
						<p>AI Professional College is a private higher education institution fast-developing a strong reputation in Business Studies and Information Technology. We are recognised for producing graduates who are competent, ethical, and career-ready.</p>
					</div>
					<div class="abmv">
						<i class="fa-solid fa-laptop-code"></i>
						<h4>Information Technology</h4>
						<p>Professional IT certifications, technical training, and BSc Computer Science — preparing students for careers in software, cybersecurity, and systems analysis.</p>
					</div>	
					<div class="abmv">
						<i class="fa-solid fa-calculator"></i>
						<h4>Accounting &amp; Finance</h4>
						<p>ACCA, CAT/FIA, CIMA, and BSc Accounting — giving students internationally recognised qualifications in accounting and finance.</p>
					</div>
					<div class="cta_two">
						<a href="course.html" class="cta"><span>View All Programs</span>
						  <svg width="13px" height="10px" viewBox="0 0 13 10">
							<path d="M1,5 L11,5"></path>
							<polyline points="8 1 12 5 8 9"></polyline>
						  </svg>
						</a>
					</div>
				</div><!-- END COL -->				
				<div class="col-lg-6 col-sm-12 col-xs-12 wow fadeInRight" data-wow-duration="1s" data-wow-delay="0.1s" data-wow-offset="0">
					<div class="ab_img">
						<img src="assets/images/pro%20images/P-1.jpeg" class="img-fluid about-img-fit" alt="AI Professional College">
					</div>
				</div><!-- END COL -->
			</div><!-- END ROW -->
		</div><!-- END CONTAINER -->
	</section>
	<!-- END QUALITY -->

	<!-- ADMISSIONS BOX -->
	<section class="insfreecourse section-padding">
		<div class="container">								
			<div class="row">								
				<div class="col-lg-6 col-sm-12 col-xs-12 wow fadeInLeft" data-wow-duration="1s" data-wow-delay="0.2s" data-wow-offset="0">
					<div class="single_ins">
						<div class="single_ins_content">
							<h4>Admissions Requirements</h4>
							<h1>Do You Qualify?</h1>
							<p>Entry to AI Professional College requires:</p>
							<ul style="margin: 10px 0 20px 20px; list-style: disc;">
								<li>Five (5) credits, maximum two sittings</li>
								<li>Minimum C5 in English Language</li>
								<li>WASSCE or GCE O-Level certificate</li>
							</ul>
							<a href="register.html" class="cta"><span>Apply Now</span>
							  <svg width="13px" height="10px" viewBox="0 0 13 10">
								<path d="M1,5 L11,5"></path>
								<polyline points="8 1 12 5 8 9"></polyline>
							  </svg>
							</a>
						</div>
						<div class="single_ins_img">
							<img src="assets/images/pro%20images/E-1.jpeg" class="img-fluid ins-img-fit" alt="Admissions">
						</div>
					</div>
				</div><!-- END COL -->				
				<div class="col-lg-6 col-sm-12 col-xs-12 wow fadeInRight" data-wow-duration="1s" data-wow-delay="0.2s" data-wow-offset="0">
					<div class="single_ins">
						<div class="single_ins_content">
							<h4>Matriculation</h4>
							<h1>Formally Join Our Community</h1>
							<p>Matriculation is the formal process of becoming a student at AI Professional College. Students are officially welcomed by the Principal, Registrar, and Student Union President in a ceremony attended by educational stakeholders.</p>
							<a href="contact.html" class="cta"><span>Contact Admissions</span>
							  <svg width="13px" height="10px" viewBox="0 0 13 10">
								<path d="M1,5 L11,5"></path>
								<polyline points="8 1 12 5 8 9"></polyline>
							  </svg>
							</a>
						</div>
						<div class="single_ins_img">
							<img src="assets/images/pro%20images/P-1%20%281%29.jpeg" class="img-fluid ins-img-fit" alt="Matriculation">
						</div>
					</div>
				</div><!-- END COL -->								  
			</div><!-- END ROW -->
		</div><!-- END CONTAINER -->
	</section>
	<!-- END ADMISSIONS BOX -->'''

COURSE_MAIN = '''	<!-- ALL PROGRAMS -->
	<section class="tp_feature section-padding">
	   <div class="container">							
		<div class="section-title text-center">
			<h4>Academic Offerings</h4>
			<h1>Explore the Right Program for Your Career.</h1>
			<p style="max-width:680px;margin:0 auto 30px;">Join our academic community, develop your potential, and achieve your dreams. We offer professional, degree, and postgraduate qualifications recognised by industry.</p>
		</div>				
		<div class="row">				
			<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.1s" data-wow-offset="0">
				<div class="single_tp">
					<h3>Professional Programs</h3>
					<i class="fa-solid fa-certificate"></i>
					<p>Industry-recognised certifications in IT and Business Studies. ACCA, CIMA, CAT/FIA, and more — earn qualifications respected worldwide.</p>
					<a href="course3.html" class="cta"><span>View Programs</span>
					  <svg width="13px" height="10px" viewBox="0 0 13 10"><path d="M1,5 L11,5"></path><polyline points="8 1 12 5 8 9"></polyline></svg>
					</a>
				</div>
			</div><!-- END COL -->			
			<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.2s" data-wow-offset="0">
				<div class="single_tp st_one">
					<h3>Degree Programs</h3>
					<i class="fa-solid fa-graduation-cap"></i>
					<p>Bachelor degree programs (BSc) in Business, Technology, and Social Sciences. Nine degree options to match your career aspirations.</p>
					<a href="course2.html" class="cta"><span>View Programs</span>
					  <svg width="13px" height="10px" viewBox="0 0 13 10"><path d="M1,5 L11,5"></path><polyline points="8 1 12 5 8 9"></polyline></svg>
					</a>
				</div>
			</div><!-- END COL -->		
			<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.3s" data-wow-offset="0">
				<div class="single_tp st_two">
					<h3>Masters Programs</h3>
					<i class="fa-solid fa-book-open"></i>
					<p>Advanced postgraduate studies for professionals. MSc Professional Accountancy prepares finance leaders for global challenges.</p>
					<a href="course.html" class="cta"><span>View Programs</span>
					  <svg width="13px" height="10px" viewBox="0 0 13 10"><path d="M1,5 L11,5"></path><polyline points="8 1 12 5 8 9"></polyline></svg>
					</a>
				</div>
			</div><!-- END COL -->		
		</div><!-- END ROW -->

		<!-- Masters detail -->
		<div class="section-title" style="margin-top:60px;">
			<h4>Postgraduate</h4>
			<h1>Master of Science in Professional Accountancy</h1>
		</div>
		<div class="row">
			<div class="col-lg-6 col-sm-12 wow fadeInLeft" data-wow-duration="1s" data-wow-delay="0.1s" data-wow-offset="0">
				<div class="ab_content">
					<h2>Advance Your Financial Career</h2>
					<p>The MSc Professional Accountancy targets finance professionals seeking advanced expertise. The program equips students to understand advanced financial models, apply management techniques, and critically assess strategic financial decisions.</p>
				</div>
				<div class="abmv">
					<i class="fa-solid fa-chart-line"></i>
					<h4>Financial Leadership</h4>
					<p>Develop leadership skills and the ability to solve complex business problems in management environments.</p>
				</div>
				<div class="abmv">
					<i class="fa-solid fa-globe"></i>
					<h4>Global Perspective</h4>
					<p>Evaluate organisational value creation and analyse strategic financial decisions from a global perspective.</p>
				</div>
				<div class="cta_two">
					<a href="register.html" class="cta"><span>Apply Now</span>
					  <svg width="13px" height="10px" viewBox="0 0 13 10"><path d="M1,5 L11,5"></path><polyline points="8 1 12 5 8 9"></polyline></svg>
					</a>
				</div>
			</div>
			<div class="col-lg-6 col-sm-12 wow fadeInRight" data-wow-duration="1s" data-wow-delay="0.2s" data-wow-offset="0">
				<div class="ab_img">
					<img src="assets/images/pro%20images/P-1.jpeg" class="img-fluid about-img-fit" alt="MSc Professional Accountancy">
				</div>
			</div>
		</div>
	   </div><!-- END CONTAINER -->
	</section>
	<!-- END ALL PROGRAMS -->'''

COURSE2_MAIN = '''	<!-- DEGREE PROGRAMS -->
	<section class="best-course section-padding">
		<div class="container">
			<div class="section-title text-center">
				<h4>Undergraduate</h4>
				<h1>BSc Degree Programs</h1>
				<p style="max-width:680px;margin:0 auto 30px;">Nine Bachelor of Science degree programs designed to meet community and student needs. All programs are built around industry demands and emerging economic trends.</p>
			</div>
			<div class="row">
				<div class="col-lg-4 col-md-6 col-12 wow fadeInUp" data-wow-duration="0.8s" data-wow-delay="0.1s" data-wow-offset="0">
					<div class="single_feature_one" style="padding:30px; background:#f9f9f9; border-radius:8px; min-height:220px;">
						<div class="sf_top">
							<i class="fa-solid fa-laptop-code" style="font-size:2rem;color:#f48024;"></i>
							<h2><a href="single_course.html">BSc Computer Science</a></h2>
						</div>
						<p>Train in web design, graphic design, server installation, biometric systems, cybersecurity, and industrial applications.</p>
						<a href="single_course.html">View Details <i class="fa-solid fa-arrow-right"></i></a>
					</div>
				</div>
				<div class="col-lg-4 col-md-6 col-12 wow fadeInUp" data-wow-duration="0.8s" data-wow-delay="0.15s" data-wow-offset="0">
					<div class="single_feature_one" style="padding:30px; background:#f9f9f9; border-radius:8px; min-height:220px;">
						<div class="sf_top">
							<i class="fa-solid fa-calculator" style="font-size:2rem;color:#f48024;"></i>
							<h2><a href="#">BSc Accounting</a></h2>
						</div>
						<p>Gain a thorough grounding in financial accounting, management accounting, auditing, and taxation principles.</p>
						<a href="register.html">Apply Now <i class="fa-solid fa-arrow-right"></i></a>
					</div>
				</div>
				<div class="col-lg-4 col-md-6 col-12 wow fadeInUp" data-wow-duration="0.8s" data-wow-delay="0.2s" data-wow-offset="0">
					<div class="single_feature_one" style="padding:30px; background:#f9f9f9; border-radius:8px; min-height:220px;">
						<div class="sf_top">
							<i class="fa-solid fa-briefcase" style="font-size:2rem;color:#f48024;"></i>
							<h2><a href="#">BSc Business Administration</a></h2>
						</div>
						<p>Gain foundational business knowledge — strategic goals, organisational policy, financial management, and leadership.</p>
						<a href="register.html">Apply Now <i class="fa-solid fa-arrow-right"></i></a>
					</div>
				</div>
				<div class="col-lg-4 col-md-6 col-12 wow fadeInUp" data-wow-duration="0.8s" data-wow-delay="0.25s" data-wow-offset="0">
					<div class="single_feature_one" style="padding:30px; background:#f9f9f9; border-radius:8px; min-height:220px;">
						<div class="sf_top">
							<i class="fa-solid fa-users" style="font-size:2rem;color:#f48024;"></i>
							<h2><a href="#">BSc Human Resource Management</a></h2>
						</div>
						<p>Develop skills in recruitment, training, employee coaching, performance monitoring, and workplace policy design.</p>
						<a href="register.html">Apply Now <i class="fa-solid fa-arrow-right"></i></a>
					</div>
				</div>
				<div class="col-lg-4 col-md-6 col-12 wow fadeInUp" data-wow-duration="0.8s" data-wow-delay="0.3s" data-wow-offset="0">
					<div class="single_feature_one" style="padding:30px; background:#f9f9f9; border-radius:8px; min-height:220px;">
						<div class="sf_top">
							<i class="fa-solid fa-chart-bar" style="font-size:2rem;color:#f48024;"></i>
							<h2><a href="#">BSc Marketing</a></h2>
						</div>
						<p>Understand consumer behaviour, develop marketing strategies, and create competitive advantages in domestic and international markets.</p>
						<a href="register.html">Apply Now <i class="fa-solid fa-arrow-right"></i></a>
					</div>
				</div>
				<div class="col-lg-4 col-md-6 col-12 wow fadeInUp" data-wow-duration="0.8s" data-wow-delay="0.35s" data-wow-offset="0">
					<div class="single_feature_one" style="padding:30px; background:#f9f9f9; border-radius:8px; min-height:220px;">
						<div class="sf_top">
							<i class="fa-solid fa-landmark" style="font-size:2rem;color:#f48024;"></i>
							<h2><a href="#">BSc Public Administration</a></h2>
						</div>
						<p>Develop expertise in government policy, public service management, and the administration of public sector organisations.</p>
						<a href="register.html">Apply Now <i class="fa-solid fa-arrow-right"></i></a>
					</div>
				</div>
				<div class="col-lg-4 col-md-6 col-12 wow fadeInUp" data-wow-duration="0.8s" data-wow-delay="0.4s" data-wow-offset="0">
					<div class="single_feature_one" style="padding:30px; background:#f9f9f9; border-radius:8px; min-height:220px;">
						<div class="sf_top">
							<i class="fa-solid fa-heart-pulse" style="font-size:2rem;color:#f48024;"></i>
							<h2><a href="#">BSc Public Health</a></h2>
						</div>
						<p>Plan health programs, analyse health information, manage projects, and improve public health outcomes at community and national level.</p>
						<a href="register.html">Apply Now <i class="fa-solid fa-arrow-right"></i></a>
					</div>
				</div>
				<div class="col-lg-4 col-md-6 col-12 wow fadeInUp" data-wow-duration="0.8s" data-wow-delay="0.45s" data-wow-offset="0">
					<div class="single_feature_one" style="padding:30px; background:#f9f9f9; border-radius:8px; min-height:220px;">
						<div class="sf_top">
							<i class="fa-solid fa-truck" style="font-size:2rem;color:#f48024;"></i>
							<h2><a href="#">BSc Procurement &amp; Logistics</a></h2>
						</div>
						<p>Gain expertise in supply chain management, procurement processes, logistics operations, and distribution management.</p>
						<a href="register.html">Apply Now <i class="fa-solid fa-arrow-right"></i></a>
					</div>
				</div>
				<div class="col-lg-4 col-md-6 col-12 wow fadeInUp" data-wow-duration="0.8s" data-wow-delay="0.5s" data-wow-offset="0">
					<div class="single_feature_one" style="padding:30px; background:#f9f9f9; border-radius:8px; min-height:220px;">
						<div class="sf_top">
							<i class="fa-solid fa-people-group" style="font-size:2rem;color:#f48024;"></i>
							<h2><a href="#">BSc Social Work</a></h2>
						</div>
						<p>Develop skills to support individuals and communities, promote social justice, and provide counselling and welfare services.</p>
						<a href="register.html">Apply Now <i class="fa-solid fa-arrow-right"></i></a>
					</div>
				</div>
				<div class="col-lg-12 text-center" style="margin-top:30px;">
					<a href="register.html" class="btn_two">Apply for a Degree Program <i class="fa-solid fa-arrow-right"></i></a>
				</div>
			</div><!-- END ROW -->
		</div><!-- END CONTAINER -->
	</section>
	<!-- END DEGREE PROGRAMS -->'''

COURSE3_MAIN = '''	<!-- PROFESSIONAL PROGRAMS -->
	<section class="tp_feature section-padding">
	   <div class="container">
		<div class="section-title text-center">
			<h4>Professional Qualifications</h4>
			<h1>Industry-Recognised Professional Programs.</h1>
			<p style="max-width:680px;margin:0 auto 30px;">Earn internationally recognised professional certifications in Accounting, Finance, and Information Technology — qualifications respected by employers worldwide.</p>
		</div>
		<div class="row">
			<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="0.8s" data-wow-delay="0.1s" data-wow-offset="0">
				<div class="single_tp">
					<h3>ACCA</h3>
					<i class="fa-solid fa-file-invoice-dollar"></i>
					<p>Association of Chartered Certified Accountants. One of the most globally recognised accounting qualifications, opening doors to careers in finance worldwide.</p>
					<a href="register.html" class="cta"><span>Apply Now</span>
					  <svg width="13px" height="10px" viewBox="0 0 13 10"><path d="M1,5 L11,5"></path><polyline points="8 1 12 5 8 9"></polyline></svg>
					</a>
				</div>
			</div><!-- END COL -->
			<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="0.8s" data-wow-delay="0.15s" data-wow-offset="0">
				<div class="single_tp st_one">
					<h3>CIMA</h3>
					<i class="fa-solid fa-chart-pie"></i>
					<p>Chartered Institute of Management Accountants. The world's largest professional body of management accountants — for business finance professionals.</p>
					<a href="register.html" class="cta"><span>Apply Now</span>
					  <svg width="13px" height="10px" viewBox="0 0 13 10"><path d="M1,5 L11,5"></path><polyline points="8 1 12 5 8 9"></polyline></svg>
					</a>
				</div>
			</div><!-- END COL -->
			<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="0.8s" data-wow-delay="0.2s" data-wow-offset="0">
				<div class="single_tp st_two">
					<h3>CAT / FIA</h3>
					<i class="fa-solid fa-receipt"></i>
					<p>Certified Accounting Technician / Foundations in Accountancy. The ideal entry-level accounting qualification before progressing to full ACCA.</p>
					<a href="register.html" class="cta"><span>Apply Now</span>
					  <svg width="13px" height="10px" viewBox="0 0 13 10"><path d="M1,5 L11,5"></path><polyline points="8 1 12 5 8 9"></polyline></svg>
					</a>
				</div>
			</div><!-- END COL -->
			<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="0.8s" data-wow-delay="0.25s" data-wow-offset="0">
				<div class="single_tp st_three">
					<h3>IT Certifications</h3>
					<i class="fa-solid fa-laptop-code"></i>
					<p>Professional IT certifications covering Microsoft Server, Web Design, Graphic Design, Security Systems, Biometric Systems, and Industrial Applications.</p>
					<a href="register.html" class="cta"><span>Apply Now</span>
					  <svg width="13px" height="10px" viewBox="0 0 13 10"><path d="M1,5 L11,5"></path><polyline points="8 1 12 5 8 9"></polyline></svg>
					</a>
				</div>
			</div><!-- END COL -->
			<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="0.8s" data-wow-delay="0.3s" data-wow-offset="0">
				<div class="single_tp">
					<h3>ABE (UK)</h3>
					<i class="fa-solid fa-globe"></i>
					<p>Association of Business Executives qualifications provide internationally recognised business education credentials for management and marketing careers.</p>
					<a href="register.html" class="cta"><span>Apply Now</span>
					  <svg width="13px" height="10px" viewBox="0 0 13 10"><path d="M1,5 L11,5"></path><polyline points="8 1 12 5 8 9"></polyline></svg>
					</a>
				</div>
			</div><!-- END COL -->
			<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="0.8s" data-wow-delay="0.35s" data-wow-offset="0">
				<div class="single_tp st_one">
					<h3>Career Development</h3>
					<i class="fa-solid fa-arrow-trend-up"></i>
					<p>All professional programs include career guidance, employer connections, and continuing education pathways to help you advance in your chosen field.</p>
					<a href="contact.html" class="cta"><span>Learn More</span>
					  <svg width="13px" height="10px" viewBox="0 0 13 10"><path d="M1,5 L11,5"></path><polyline points="8 1 12 5 8 9"></polyline></svg>
					</a>
				</div>
			</div><!-- END COL -->
			<div class="col-lg-12 text-center" style="margin-top:30px;">
				<a href="register.html" class="btn_two">Apply for a Professional Program <i class="fa-solid fa-arrow-right"></i></a>
			</div>
		</div><!-- END ROW -->
	   </div><!-- END CONTAINER -->
	</section>
	<!-- END PROFESSIONAL PROGRAMS -->'''

CONTACT_MAIN = '''	<!-- CONTACT SECTION -->
	<section class="section-padding">
		<div class="container">
			<div class="row">
				<div class="col-lg-6 col-sm-12 wow fadeInLeft" data-wow-duration="1s" data-wow-delay="0.1s" data-wow-offset="0">
					<div class="ab_content">
						<h2>Get in Touch with AI Professional College</h2>
						<p>We welcome all enquiries from prospective students, current students, parents, and industry partners. Our admissions team is ready to assist you find the right program.</p>
					</div>
					<div class="abmv">
						<i class="fa-solid fa-phone"></i>
						<h4>Phone Number</h4>
						<p>+233 (0) 000 000 000</p>
					</div>
					<div class="abmv">
						<i class="fa-solid fa-envelope"></i>
						<h4>Email Address</h4>
						<p><a href="mailto:info@aiprofessionals.org">info@aiprofessionals.org</a></p>
					</div>
					<div class="abmv">
						<i class="fa-solid fa-location-dot"></i>
						<h4>Our Address</h4>
						<p>AI Professional College, Ghana</p>
					</div>
					<div class="abmv">
						<i class="fa-solid fa-clock"></i>
						<h4>Office Hours</h4>
						<p>Monday – Friday: 8:00am – 5:00pm</p>
					</div>
				</div><!-- END COL -->
				<div class="col-lg-6 col-sm-12 wow fadeInRight" data-wow-duration="1s" data-wow-delay="0.2s" data-wow-offset="0">
					<div class="contact_form" style="background:#f9f9f9; padding:40px; border-radius:12px;">
						<h3 style="margin-bottom:25px;">Send Us a Message</h3>
						<form id="contact-form" action="contact.php" method="POST">
							<div class="row">
								<div class="col-md-6">
									<div class="form-group" style="margin-bottom:20px;">
										<input type="text" name="name" class="form-control" id="name" placeholder="Your Full Name" style="padding:12px; border-radius:6px; border:1px solid #ddd;" required>
									</div>
								</div>
								<div class="col-md-6">
									<div class="form-group" style="margin-bottom:20px;">
										<input type="email" name="email" class="form-control" id="email" placeholder="Your Email Address" style="padding:12px; border-radius:6px; border:1px solid #ddd;" required>
									</div>
								</div>
								<div class="col-md-12">
									<div class="form-group" style="margin-bottom:20px;">
										<input type="text" name="subject" class="form-control" id="subject" placeholder="Subject" style="padding:12px; border-radius:6px; border:1px solid #ddd;">
									</div>
								</div>
								<div class="col-md-12">
									<div class="form-group" style="margin-bottom:25px;">
										<textarea name="message" class="form-control" id="message" rows="5" placeholder="Your Message" style="padding:12px; border-radius:6px; border:1px solid #ddd; resize:vertical;"></textarea>
									</div>
								</div>
								<div class="col-md-12">
									<button type="submit" class="btn_two" id="submit-btn" style="width:100%; padding:14px; cursor:pointer;">Send Message <i class="fa-solid fa-paper-plane"></i></button>
								</div>
							</div>
						</form>
					</div>
				</div><!-- END COL -->
			</div><!-- END ROW -->
		</div><!-- END CONTAINER -->
	</section>
	<!-- END CONTACT -->'''

FAQ_MAIN = '''	<!-- ADMISSIONS FAQ -->
	<section class="faq_area section-padding">
		<div class="container">								
			<div class="section-title">
				<h4>Admissions</h4>
				<h1>Frequently Asked Admissions Questions</h1>
			</div>			
			<div class="row justify-content-center">
				<div class="col-lg-6 col-sm-6 col-xs-12">
					<div class="accordion" id="accordionFAQ">
					  <div class="accordion-item">
						<h2 class="accordion-header" id="faqH1">
						  <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#faqC1" aria-expanded="true" aria-controls="faqC1">
							What are the entry requirements?
						  </button>
						</h2>
						<div id="faqC1" class="accordion-collapse collapse show" aria-labelledby="faqH1" data-bs-parent="#accordionFAQ">
						  <div class="accordion-body">
							To gain entry to AI Professional College, you need five (5) credits in a maximum of two sittings, a minimum C5 in English Language, and a WASSCE or GCE O-Level certificate.
						  </div>
						</div>
					  </div>
					  <div class="accordion-item">
						<h2 class="accordion-header" id="faqH2">
						  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faqC2" aria-expanded="false" aria-controls="faqC2">
							What programs does AIPC offer?
						  </button>
						</h2>
						<div id="faqC2" class="accordion-collapse collapse" aria-labelledby="faqH2" data-bs-parent="#accordionFAQ">
						  <div class="accordion-body">
							AIPC offers three types of programs: Professional Programs (ACCA, CIMA, CAT/FIA, IT certifications), Degree Programs (9 BSc degrees including Computer Science, Accounting, Business Admin, HRM, Marketing, Public Health, and more), and Masters Programs (MSc Professional Accountancy).
						  </div>
						</div>
					  </div>
					  <div class="accordion-item">
						<h2 class="accordion-header" id="faqH3">
						  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faqC3" aria-expanded="false" aria-controls="faqC3">
							When was AI Professional College established?
						  </button>
						</h2>
						<div id="faqC3" class="accordion-collapse collapse" aria-labelledby="faqH3" data-bs-parent="#accordionFAQ">
						  <div class="accordion-body">
							AI Professional College was established in 2014. Since then, it has grown into a private higher education institution specialising in Business Studies and Information Technology, with a fast-developing reputation for producing career-ready graduates.
						  </div>
						</div>
					  </div>
					  <div class="accordion-item">
						<h2 class="accordion-header" id="faqH4">
						  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faqC4" aria-expanded="false" aria-controls="faqC4">
							How do I apply?
						  </button>
						</h2>
						<div id="faqC4" class="accordion-collapse collapse" aria-labelledby="faqH4" data-bs-parent="#accordionFAQ">
						  <div class="accordion-body">
							You can apply online via our Apply Now page or visit our admissions office directly. Our admissions team will guide you through the application process and help you select the right program for your career goals.
						  </div>
						</div>
					  </div>
					  <div class="accordion-item">
						<h2 class="accordion-header" id="faqH5">
						  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faqC5" aria-expanded="false" aria-controls="faqC5">
							Does AIPC offer professional accounting qualifications?
						  </button>
						</h2>
						<div id="faqC5" class="accordion-collapse collapse" aria-labelledby="faqH5" data-bs-parent="#accordionFAQ">
						  <div class="accordion-body">
							Yes! AIPC is professionally affiliated with ACCA, CIMA, and CAT/FIA — among the most respected accounting bodies in the world. You can study for these qualifications at our campus.
						  </div>
						</div>
					  </div>
					  <div class="accordion-item">
						<h2 class="accordion-header" id="faqH6">
						  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faqC6" aria-expanded="false" aria-controls="faqC6">
							What student support services are available?
						  </button>
						</h2>
						<div id="faqC6" class="accordion-collapse collapse" aria-labelledby="faqH6" data-bs-parent="#accordionFAQ">
						  <div class="accordion-body">
							AIPC offers comprehensive student support including academic guidance, counselling, student success initiatives, orientation week activities, student clubs, leadership programs, and a secured campus environment with security personnel on site.
						  </div>
						</div>
					  </div>
					</div>				
				</div><!-- END COL -->	
				<div class="col-lg-6 col-sm-6 col-xs-12">
					<div class="pt_faq">
						<img src="assets/images/pro%20images/P-1.jpeg" class="img-fluid about-img-fit" alt="Admissions FAQ" />
					</div>
				</div><!-- END COL -->	
			</div><!--END ROW  -->
		</div><!-- END CONTAINER -->
	</section>
	<!-- END FAQ -->

	<!-- APPLY CTA -->
	<section class="insfreecourse section-padding">
		<div class="container">
			<div class="row">
				<div class="col-lg-6 col-sm-12 col-xs-12 wow fadeInLeft" data-wow-duration="1s" data-wow-delay="0.1s" data-wow-offset="0">
					<div class="single_ins">
						<div class="single_ins_content">
							<h4>Ready to Begin?</h4>
							<h1>Apply Now</h1>
							<p>Take the first step toward your future career. Apply to AI Professional College and join a community of ambitious professionals.</p>
							<a href="register.html" class="cta"><span>Start Application</span>
							  <svg width="13px" height="10px" viewBox="0 0 13 10"><path d="M1,5 L11,5"></path><polyline points="8 1 12 5 8 9"></polyline></svg>
							</a>
						</div>
						<div class="single_ins_img">
							<img src="assets/images/pro%20images/E-1.jpeg" class="img-fluid ins-img-fit" alt="Apply Now">
						</div>
					</div>
				</div>
				<div class="col-lg-6 col-sm-12 col-xs-12 wow fadeInRight" data-wow-duration="1s" data-wow-delay="0.2s" data-wow-offset="0">
					<div class="single_ins">
						<div class="single_ins_content">
							<h4>Still Have Questions?</h4>
							<h1>Contact Admissions</h1>
							<p>Our admissions team is available Monday to Friday, 8am–5pm. We are happy to answer any questions about programs, entry requirements, or fees.</p>
							<a href="contact.html" class="cta"><span>Contact Us</span>
							  <svg width="13px" height="10px" viewBox="0 0 13 10"><path d="M1,5 L11,5"></path><polyline points="8 1 12 5 8 9"></polyline></svg>
							</a>
						</div>
						<div class="single_ins_img">
							<img src="assets/images/pro%20images/P-1%20%281%29.jpeg" class="img-fluid ins-img-fit" alt="Contact Admissions">
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>
	<!-- END APPLY CTA -->'''

REGISTER_MAIN = '''	<!-- APPLY NOW -->
	<section class="section-padding">
		<div class="container">
			<div class="row justify-content-center">
				<div class="col-lg-6 col-sm-12 wow fadeInLeft" data-wow-duration="1s" data-wow-delay="0.1s" data-wow-offset="0">
					<div class="ab_content" style="margin-bottom:30px;">
						<h2>Apply to AI Professional College</h2>
						<p>Complete the form below to begin your application. Our admissions team will review your details and contact you within 2-3 working days with next steps.</p>
					</div>
					<div class="abmv">
						<i class="fa-solid fa-list-check"></i>
						<h4>Entry Requirements</h4>
						<p>Five (5) credits (max 2 sittings), minimum C5 in English Language, WASSCE or GCE O-Level.</p>
					</div>
					<div class="abmv">
						<i class="fa-solid fa-graduation-cap"></i>
						<h4>Program Options</h4>
						<p>Professional Programs, BSc Degree Programs (9 options), and MSc Professional Accountancy.</p>
					</div>
					<div class="abmv">
						<i class="fa-solid fa-clock"></i>
						<h4>Admissions Office Hours</h4>
						<p>Monday – Friday: 8:00am – 5:00pm<br><a href="mailto:info@aiprofessionals.org">info@aiprofessionals.org</a></p>
					</div>
				</div>
				<div class="col-lg-6 col-sm-12 wow fadeInRight" data-wow-duration="1s" data-wow-delay="0.2s" data-wow-offset="0">
					<div class="contact_form" style="background:#f9f9f9; padding:40px; border-radius:12px;">
						<h3 style="margin-bottom:25px;">Application Form</h3>
						<form id="apply-form">
							<div class="row">
								<div class="col-md-6">
									<div class="form-group" style="margin-bottom:20px;">
										<input type="text" class="form-control" id="first-name" placeholder="First Name" style="padding:12px;border-radius:6px;border:1px solid #ddd;" required>
									</div>
								</div>
								<div class="col-md-6">
									<div class="form-group" style="margin-bottom:20px;">
										<input type="text" class="form-control" id="last-name" placeholder="Last Name" style="padding:12px;border-radius:6px;border:1px solid #ddd;" required>
									</div>
								</div>
								<div class="col-md-12">
									<div class="form-group" style="margin-bottom:20px;">
										<input type="email" class="form-control" id="apply-email" placeholder="Email Address" style="padding:12px;border-radius:6px;border:1px solid #ddd;" required>
									</div>
								</div>
								<div class="col-md-12">
									<div class="form-group" style="margin-bottom:20px;">
										<input type="tel" class="form-control" id="apply-phone" placeholder="Phone Number" style="padding:12px;border-radius:6px;border:1px solid #ddd;">
									</div>
								</div>
								<div class="col-md-12">
									<div class="form-group" style="margin-bottom:20px;">
										<select class="form-control" id="program" style="padding:12px;border-radius:6px;border:1px solid #ddd; background:#fff;">
											<option value="">-- Select Program of Interest --</option>
											<optgroup label="Degree Programs">
												<option>BSc Computer Science</option>
												<option>BSc Accounting</option>
												<option>BSc Business Administration</option>
												<option>BSc Human Resource Management</option>
												<option>BSc Marketing</option>
												<option>BSc Public Administration</option>
												<option>BSc Public Health</option>
												<option>BSc Procurement &amp; Logistics</option>
												<option>BSc Social Work</option>
											</optgroup>
											<optgroup label="Professional Programs">
												<option>ACCA</option>
												<option>CIMA</option>
												<option>CAT / FIA</option>
												<option>IT Certifications</option>
											</optgroup>
											<optgroup label="Masters">
												<option>MSc Professional Accountancy</option>
											</optgroup>
										</select>
									</div>
								</div>
								<div class="col-md-12">
									<div class="form-group" style="margin-bottom:25px;">
										<textarea class="form-control" id="apply-message" rows="4" placeholder="Tell us about yourself and your academic background" style="padding:12px;border-radius:6px;border:1px solid #ddd;resize:vertical;"></textarea>
									</div>
								</div>
								<div class="col-md-12">
									<button type="submit" class="btn_two" id="apply-submit" style="width:100%;padding:14px;cursor:pointer;">Submit Application <i class="fa-solid fa-paper-plane"></i></button>
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
	</section>
	<!-- END APPLY NOW -->'''

TEAM_SECTION_TITLE = ('Our Faculty &amp; Staff', 'Our Expert Lecturers &amp; Academic Staff')
TEAM_MEMBERS = [
    ('Dr. Kwame Asante', 'Head of Computer Science', 'BSc &amp; IT Programs', 'assets/images/pro%20images/P-1%20%281%29.jpeg'),
    ('Mrs. Abena Mensah', 'Head of Accounting', 'ACCA &amp; CIMA Programs', 'assets/images/pro%20images/F-1-768x837.jpeg'),
    ('Mr. Kofi Boateng', 'Head of Business Administration', 'BSc Business Admin', 'assets/images/pro%20images/P-1.jpeg'),
    ('Dr. Ama Owusu', 'Head of Public Health', 'BSc Public Health', 'assets/images/pro%20images/P-1%20%281%29.jpeg'),
    ('Mr. Yaw Darko', 'Head of Human Resource Management', 'BSc HRM', 'assets/images/pro%20images/X-1.jpeg'),
    ('Mrs. Akua Sarpong', 'Head of Marketing', 'BSc Marketing', 'assets/images/pro%20images/E-1.jpeg'),
    ('Mr. Kwesi Mensah', 'Head of Procurement &amp; Logistics', 'BSc Procurement', 'assets/images/pro%20images/O-1.jpeg'),
    ('Dr. Adwoa Boateng', 'Senior Lecturer, Economics', 'BSc Economics', 'assets/images/pro%20images/N%20%281%29.jpeg'),
]

def build_team_section():
    cards = ''
    delays = [0.1, 0.2, 0.3, 0.4, 0.1, 0.2, 0.3, 0.4]
    for i, (name, role, dept, img) in enumerate(TEAM_MEMBERS):
        delay = delays[i % len(delays)]
        cards += f'''			<div class="col-lg-3 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="1s" data-wow-delay="{delay}s" data-wow-offset="0">
				<div class="our-team">
					<div class="team_img">
						<img src="{img}" alt="{name}" class="team-img-fit">
						<ul class="social">
							<li><a href="#" class="top_f_facebook"><i class="fa-brands fa-facebook"></i></a></li>
							<li><a href="#" class="top_f_linkedin"><i class="fa-brands fa-linkedin-in"></i></a></li>
						</ul>
					</div>
					<div class="team-content">
						<h3 class="title">{name}</h3>
						<span class="post">{role}</span>
						<div class="sth_det2">
							<span class="ti-book"> <u>{dept}</u></span>
						</div>
					</div>
				</div>
			</div><!-- END COL -->
'''
    return f'''	<!-- FACULTY & STAFF -->
	<section class="team_member section-padding">
	   <div class="container">
			<div class="section-title">
				<h4>{TEAM_SECTION_TITLE[0]}</h4>
				<h1>{TEAM_SECTION_TITLE[1]}</h1>
			</div>		
			<div class="row text-center">								
{cards}			</div><!-- END ROW -->
		</div><!-- END CONTAINER -->
	</section>
	<!-- END FACULTY & STAFF -->'''

# Page-specific content main body (between section-top and footer)
PAGE_CONTENT = {
    'about.html':       ABOUT_MAIN,
    'course.html':      COURSE_MAIN,
    'course2.html':     COURSE2_MAIN,
    'course3.html':     COURSE3_MAIN,
    'contact.html':     CONTACT_MAIN,
    'faq.html':         FAQ_MAIN,
    'register.html':    REGISTER_MAIN,
    'team.html':        build_team_section(),
}

SECTION_TOP_PATTERN = re.compile(
    r'<!-- START SECTION TOP -->.*?<!-- END SECTION TOP -->',
    re.DOTALL
)
META_TITLE_PATTERN = re.compile(
    r'<meta name="description" content="[^"]*">.*?<title>[^<]*</title>',
    re.DOTALL
)

def find_content_zone(html, page):
    """Find the zone between END SECTION TOP and START FOOTER to replace."""
    start_marker = '<!-- END SECTION TOP -->'
    end_marker = '<!-- START FOOTER -->'
    idx_start = html.find(start_marker)
    idx_end = html.find(end_marker)
    if idx_start == -1 or idx_end == -1:
        return None, None, None
    content_start = idx_start + len(start_marker)
    return html[:content_start], PAGE_CONTENT[page], html[idx_end:]

updated = []
skipped = []

for page, (title, desc) in PAGE_TITLES.items():
    fpath = os.path.join(BASE, page)
    if not os.path.exists(fpath):
        skipped.append(page)
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update meta/title
    new_meta = f'<meta name="description" content="{desc}">\n\t\t<meta name="keywords" content="AI Professional College, university, higher education, Ghana">\n\t\t<meta name="author" content="AI Professional College">\n\t\t<!-- SITE TITLE -->\n\t\t<title>{title}</title>'
    html = META_TITLE_PATTERN.sub(new_meta, html)

    # 2. Update top contact
    html = html.replace(OLD_PHONE, NEW_PHONE).replace(OLD_EMAIL, NEW_EMAIL).replace(OLD_HOURS, NEW_HOURS)
    html = html.replace(OLD_TEL, NEW_TEL).replace(OLD_MAILTO, NEW_MAILTO)
    html = html.replace('+ 485 7548 8546', NEW_PHONE)
    html = html.replace('example@gmail.com', 'info@aiprofessionals.org')

    # 3. Update section top
    if page in SECTION_TOPS:
        t, pl, ph, cur = SECTION_TOPS[page]
        new_top = build_section_top(t, pl, ph, cur)
        # Try replacing existing section-top
        new_html = SECTION_TOP_PATTERN.sub(new_top, html)
        if new_html != html:
            html = new_html

    # 4. Replace main content zone if we have content for this page
    if page in PAGE_CONTENT:
        before, content, after = find_content_zone(html, page)
        if before is not None:
            html = before + '\n\n' + content + '\n\n\t' + after

    # 5. Update footer
    new_html = FOOTER_PATTERN.sub(FOOTER, html)
    if new_html != html:
        html = new_html

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    updated.append(page)
    print(f'  [OK] {page}')

print(f'\nDone! Updated: {len(updated)}, Skipped: {skipped}')
