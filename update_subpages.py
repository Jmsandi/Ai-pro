import os, re

PAGE_CONTENT = {
    'team-details.html': '''	<!-- START INSTRUCTOR DETAILS -->
	<section class="team_member_details section-padding">
	   <div class="container">
			<div class="row">
				<div class="col-lg-5 col-sm-12 col-xs-12 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.1s" data-wow-offset="0">
					<div class="single_ins_img">
						<img src="assets/images/pro%20images/P-1%20%281%29.jpeg" alt="Dr. Kwame Asante">
					</div>
				</div><!-- END COL -->
				<div class="col-lg-7 col-sm-12 col-xs-12 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.2s" data-wow-offset="0">
					<div class="team_member_info">
						<h3 class="title">Dr. Kwame Asante</h3>
						<span class="post">Head of Computer Science</span>
						<p>Dr. Kwame Asante holds a Ph.D. in Computer Science and has over 15 years of industry experience in software engineering and IT consultancy. He brings a wealth of practical knowledge to AI Professional College, focusing on modern web development, network infrastructure, and biometric systems.</p>
						
						<p>He is passionate about developing students who are not only technically proficient but also ethically grounded. His goal is to ensure every graduate is ready for immediate workplace impact.</p>
						
						<div class="ins_skills">
							<h4>Areas of Expertise:</h4>
							<ul>
								<li><i class="fa fa-check"></i> Cyber Security & Network Systems</li>
								<li><i class="fa fa-check"></i> Software Engineering</li>
								<li><i class="fa fa-check"></i> Database Administration</li>
								<li><i class="fa fa-check"></i> Educational Technology</li>
							</ul>
						</div>
					</div>
				</div><!-- END COL -->
			</div><!-- END ROW -->
		</div><!-- END CONTAINER -->
	</section>
	<!-- END INSTRUCTOR DETAILS -->''',

    'event.html': '''	<!-- START EVENT -->
	<section class="our-event section-padding">
		<div class="container">				
			<div class="row">				
				<div class="col-lg-4 col-sm-6 col-xs-12">
					<div class="event-slide">
						<div class="event-img">
							<img src="assets/images/pro%20images/X-1.jpeg" alt="Event Image" class="about-img-fit">
							<div class="event-date">
								<span class="date">16</span>
								<span class="month">Apr</span>
							</div>
						</div>
						<div class="event-content">
							<h3><a href="event_single.html">Annual Matriculation Ceremony</a></h3>
							<span><i class="fa fa-clock-o"></i>9.00AM - 1.00PM</span>
							<span><i class="fa fa-table"></i><strong>AI Professional College Campus</strong></span>
							<p>The formal process of welcoming new students to AI Professional College. Join the Principal, Registrar, and Student Union President.</p>
						</div>
					</div><!-- END EVENT -->
				</div><!-- END COL -->	
				<div class="col-lg-4 col-sm-6 col-xs-12">
					<div class="event-slide">
						<div class="event-img">
							<img src="assets/images/pro%20images/E-1.jpeg" alt="Event Image" class="about-img-fit">
							<div class="event-date">
								<span class="date">05</span>
								<span class="month">May</span>
							</div>
						</div>
						<div class="event-content">
							<h3><a href="event_single.html">Tech Innovation Summit 2026</a></h3>
							<span><i class="fa fa-clock-o"></i>10.00AM - 3.00PM</span>
							<span><i class="fa fa-table"></i><strong>Main Auditorium</strong></span>
							<p>A showcase of student IT projects, software development, and network infrastructure designs for industry partners.</p>
						</div>
					</div><!-- END EVENT -->
				</div><!-- END COL -->	
				<div class="col-lg-4 col-sm-6 col-xs-12">
					<div class="event-slide">
						<div class="event-img">
							<img src="assets/images/pro%20images/1781279715938.jpg" alt="Event Image" class="about-img-fit">
							<div class="event-date">
								<span class="date">12</span>
								<span class="month">Jun</span>
							</div>
						</div>
						<div class="event-content">
							<h3><a href="event_single.html">Business Leadership Seminar</a></h3>
							<span><i class="fa fa-clock-o"></i>2.00PM - 4.00PM</span>
							<span><i class="fa fa-table"></i><strong>Lecture Hall A</strong></span>
							<p>Guest speakers from leading financial institutions discussing the future of Accounting and Business Administration in Ghana.</p>
						</div>
					</div><!-- END EVENT -->
				</div><!-- END COL -->	
			</div><!-- END ROW -->
		</div><!-- END CONTAINER -->			
	</section>
	<!-- END EVENT -->''',

    'event_single.html': '''	<!-- START EVENT -->
	<section class="our-event section-padding">
		<div class="container">				
			<div class="row">
				<div class="col-lg-8 col-sm-12 col-xs-12">
					<div class="single_event_single">
						<img src="assets/images/pro%20images/X-1.jpeg" class="img-fluid about-img-fit" alt="Event Image" />
						<div class="single_event_text_single">
							<h4>Annual Matriculation Ceremony</h4>
							<span><i class="fa fa-calendar"></i>16 April 2026</span>
							<span><i class="fa fa-clock-o"></i>9.00AM - 1.00PM</span>
							<span><i class="fa fa-table"></i><strong>AI Professional College Campus</strong></span>
							<p>Matriculation is the formal process of becoming a student at AI Professional College. Students will be officially welcomed by the Principal, Registrar, and Student Union President.</p>
							<p>Stakeholders present will include the Parliamentary Oversight Committee for Higher Education, Ministry of Higher Education, Tertiary Education Committee, and NCTVA representatives. We invite all new students to formally join the institution during this prestigious ceremony.</p>
						</div>
					</div><!-- END SINGLE EVENT -->
				</div><!-- END COL -->
				<div class="col-lg-4 col-sm-12 col-xs-12">
					<div class="event_info">
						<h3>Event Details</h3>
						<ul>
							<li><i class="fa fa-calendar"></i> <strong>Date:</strong> 16 April 2026</li>
							<li><i class="fa fa-clock-o"></i> <strong>Time:</strong> 9.00AM - 1.00PM</li>
							<li><i class="fa fa-map-marker"></i> <strong>Location:</strong> AI Professional College Campus</li>
							<li><i class="fa fa-phone"></i> <strong>Phone:</strong> +233 (0) 000 000 000</li>
							<li><i class="fa fa-envelope"></i> <strong>Email:</strong> info@aiprofessionals.org</li>
						</ul>
					</div>
				</div><!-- END COL -->
			</div><!-- END ROW -->
		</div><!-- END CONTAINER -->
	</section>
	<!-- END EVENT -->''',

    'faq.html': '''	<!-- START FAQ -->
	<section class="faq_area section-padding">
		<div class="container">
			<div class="section-title">
				<h4>Admissions FAQ</h4>
				<h1>Frequently Asked Questions</h1>
			</div>		
			<div class="row justify-content-center">
				<div class="col-lg-8 col-sm-12 col-xs-12">
					<div class="accordion" id="accordionExample">
					  <div class="accordion-item">
						<h2 class="accordion-header" id="headingOne">
						  <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
							What are the entry level qualifications?
						  </button>
						</h2>
						<div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
						  <div class="accordion-body">
							The entry-level qualification for our programs requires a minimum of Five (5) credits, obtained in a maximum of two sittings. You must also have a minimum of C5 in English Language. Both WASSCE and GCE O-Level results are accepted.
						  </div>
						</div>
					  </div>
					  <div class="accordion-item">
						<h2 class="accordion-header" id="headingTwo">
						  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
							Do you offer Degree and Professional Programs?
						  </button>
						</h2>
						<div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
						  <div class="accordion-body">
							Yes! We offer a wide range of programs. Our Degree Programs include BSc Computer Science, BSc Accounting, BSc Business Administration, BSc Human Resource Management, and more. Our Professional Programs include ACCA, CIMA, and industry-recognized IT certifications.
						  </div>
						</div>
					  </div>
					  <div class="accordion-item">
						<h2 class="accordion-header" id="headingThree">
						  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
							Are there pathways for career advancement?
						  </button>
						</h2>
						<div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample">
						  <div class="accordion-body">
							Absolutely. We focus on practical education designed around industry demands. We develop career-focused graduates equipped with practical professional skills and ethical standards, ready for immediate workplace impact.
						  </div>
						</div>
					  </div>
					  <div class="accordion-item">
						<h2 class="accordion-header" id="headingFour">
						  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour">
							Is financial aid or scholarships available?
						  </button>
						</h2>
						<div id="collapseFour" class="accordion-collapse collapse" aria-labelledby="headingFour" data-bs-parent="#accordionExample">
						  <div class="accordion-body">
							We provide equal educational opportunities for all students. Please contact the Admissions Office at info@aiprofessionals.org to discuss flexible payment plans and available opportunities.
						  </div>
						</div>
					  </div>
					</div>
				</div><!-- END COL -->
			</div><!-- END ROW -->
		</div><!-- END CONTAINER -->
	</section>
	<!-- END FAQ -->''',

    'login.html': '''	<!-- START LOGIN -->
	<div class="login_register_area section-padding">
		<div class="container">
			<div class="row justify-content-center">
				<div class="col-lg-6 col-sm-12 col-xs-12">
					<div class="log_form">
						<h2>Student Portal Login</h2>
						<p>Access your course materials, grades, and academic records.</p>
						<form>
							<div class="form-group">
								<label>Student ID or Email</label>
								<input type="text" class="form-control" placeholder="Enter your Student ID">
							</div>
							<div class="form-group">
								<label>Password</label>
								<input type="password" class="form-control" placeholder="Password">
							</div>
							<div class="login_opt">
								<div class="checkbox">
									<label><input type="checkbox" value=""> Remember Me</label>
								</div>
								<a href="#">Forgot Password?</a>
							</div>
							<div class="text-center">
								<button type="submit" class="btn_two">Login</button>
							</div>
							<div class="create_acc">
								<p>Don't have an account? <a href="contact.html">Contact Admissions</a></p>
							</div>
						</form>
					</div>
				</div><!-- END COL -->
			</div><!-- END ROW -->
		</div><!-- END CONTAINER -->
	</div>
	<!-- END LOGIN -->''',

    'error.html': '''	<!-- START 404 -->
	<section class="zero_area section-padding">
		<div class="container">
			<div class="row">
				<div class="col-lg-12 col-sm-12 col-xs-12 text-center">
					<div class="error_page">
						<img src="assets/images/all-img/404.svg" alt="404 Error">
						<h2>Oops! Page Not Found</h2>
						<p>The lecture hall or page you are looking for might have been removed, had its name changed, or is temporarily unavailable.</p>
						<div class="home_btn">
							<a href="index.html" class="btn_two">Back to Home</a>
						</div>
					</div>
				</div><!--- END COL -->
			</div><!--- END ROW -->
		</div><!--- END CONTAINER -->
	</section>
	<!-- END 404 -->''',

    'blog.html': '''	<!-- START NEWS -->
	<section class="blog_area section-padding">
		<div class="container">
			<div class="section-title text-center">
				<h4>News &amp; Events</h4>
				<h1>Latest Updates from AI Professional College</h1>
			</div>		
			<div class="row">		
				<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.1s" data-wow-offset="0">
					<div class="single_blog">
						<img src="assets/images/pro%20images/P-1.jpeg" class="img-fluid blog-img-fit" alt="News Image">
						<div class="content_box">
							<span>August 25, 2025 | <a href="#">Academic News</a></span>
							<h2><a href="blog_single.html">AI Professional College Announces New BSc Computer Science Program</a></h2>
							<p>We are thrilled to launch our new BSc Computer Science program designed to equip students with modern IT skills and biometric systems training.</p>
							<a href="blog_single.html" class="cta"><span>Read More</span>
							  <svg width="13px" height="10px" viewBox="0 0 13 10">
								<path d="M1,5 L11,5"></path>
								<polyline points="8 1 12 5 8 9"></polyline>
							  </svg>
							</a>
						</div>
					</div>
				</div><!-- END COL -->
				<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.2s" data-wow-offset="0">
					<div class="single_blog">
						<img src="assets/images/pro%20images/O-1.jpeg" class="img-fluid blog-img-fit" alt="News Image">
						<div class="content_box">
							<span>September 10, 2025 | <a href="#">Student Success</a></span>
							<h2><a href="blog_single.html">Graduates Secure Top Roles in Finance and IT Sectors</a></h2>
							<p>Our recent batch of ACCA and CIMA professional program graduates have successfully secured roles in leading organizations across Ghana.</p>
							<a href="blog_single.html" class="cta"><span>Read More</span>
							  <svg width="13px" height="10px" viewBox="0 0 13 10">
								<path d="M1,5 L11,5"></path>
								<polyline points="8 1 12 5 8 9"></polyline>
							  </svg>
							</a>
						</div>
					</div>
				</div><!-- END COL -->
				<div class="col-lg-4 col-sm-6 col-xs-12 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.3s" data-wow-offset="0">
					<div class="single_blog">
						<img src="assets/images/pro%20images/1781279715938.jpg" class="img-fluid blog-img-fit" alt="News Image">
						<div class="content_box">
							<span>October 05, 2025 | <a href="#">Campus Life</a></span>
							<h2><a href="blog_single.html">Cultural Enrichment and Community Development Initiatives</a></h2>
							<p>The student union recently hosted a cultural enrichment week aimed at strengthening relationships between students, faculty, and the local community.</p>
							<a href="blog_single.html" class="cta"><span>Read More</span>
							  <svg width="13px" height="10px" viewBox="0 0 13 10">
								<path d="M1,5 L11,5"></path>
								<polyline points="8 1 12 5 8 9"></polyline>
							  </svg>
							</a>
						</div>
					</div>
				</div><!-- END COL -->
			</div><!-- END ROW -->
		</div><!-- END CONTAINER -->
	</section>
	<!-- END NEWS -->''',

    'blog_single.html': '''	<!-- START NEWS DETAILS -->
	<section class="blog_single_area section-padding">
		<div class="container">
			<div class="row">
				<div class="col-lg-8 col-sm-12 col-xs-12">
					<div class="blog_single_content">
						<img src="assets/images/pro%20images/P-1.jpeg" class="img-fluid about-img-fit" alt="News Image">
						<div class="blog_single_text">
							<h2>AI Professional College Announces New BSc Computer Science Program</h2>
							<ul class="blog_meta">
								<li><i class="fa fa-user"></i> College Administration</li>
								<li><i class="fa fa-calendar"></i> August 25, 2025</li>
								<li><i class="fa fa-folder-open"></i> Academic News</li>
							</ul>
							<p>We are thrilled to launch our new BSc Computer Science program designed to equip students with modern IT skills and biometric systems training.</p>
							
							<blockquote>"The goal is to help students develop career-focused skills, improve their quality of life, and impact society positively. We are committed to producing business and technology experts."</blockquote>
							
							<p>Students in the new program will be trained in Microsoft Server Installation, Web Design, Graphic Design, Industrial Applications, Security Systems, and Biometric Systems.</p>
							<p>The program aims to provide a strong IT foundation, build internationally competitive graduates, deliver modern technical skills, and create immediate workplace impact.</p>
						</div>
					</div>
				</div><!-- END COL -->
				<div class="col-lg-4 col-sm-12 col-xs-12">
					<div class="sidebar_widget">
						<h3 class="widget_title">Recent News</h3>
						<div class="recent_post_widget">
							<div class="single_recent_post">
								<img src="assets/images/pro%20images/O-1.jpeg" alt="" style="width:70px; height:70px; object-fit:cover;">
								<div class="rp_text">
									<h4><a href="blog_single.html">Graduates Secure Top Roles in Finance</a></h4>
									<span>Sep 10, 2025</span>
								</div>
							</div>
							<div class="single_recent_post">
								<img src="assets/images/pro%20images/1781279715938.jpg" alt="" style="width:70px; height:70px; object-fit:cover;">
								<div class="rp_text">
									<h4><a href="blog_single.html">Cultural Enrichment Week</a></h4>
									<span>Oct 05, 2025</span>
								</div>
							</div>
						</div>
					</div>
				</div><!-- END COL -->
			</div><!-- END ROW -->
		</div><!-- END CONTAINER -->
	</section>
	<!-- END NEWS DETAILS -->'''
}

def replace_content_zone(html_content, page_name):
    # Find start and end markers
    start_marker = '<!-- END  TOP HEADER CLASS -->'
    end_marker = '<!-- START FOOTER -->'
    
    idx_start = html_content.find(start_marker)
    idx_end = html_content.find(end_marker)
    
    if idx_start == -1 or idx_end == -1:
        return None
        
    before = html_content[:idx_start + len(start_marker)]
    after = html_content[idx_end:]
    
    new_content = PAGE_CONTENT[page_name]
    
    return before + '\n\n' + new_content + '\n\n\t' + after

for page, content in PAGE_CONTENT.items():
    if os.path.exists(page):
        with open(page, 'r', encoding='utf-8') as f:
            html = f.read()
            
        new_html = replace_content_zone(html, page)
        
        if new_html:
            with open(page, 'w', encoding='utf-8') as f:
                f.write(new_html)
            print(f"Updated {page}")
        else:
            print(f"Failed to find markers in {page}")

