%include('header.tpl')
<div class="content-wrapper">

<section class="content">
<section class="header">
<h3>Host: jarvis </h3>
</section>

<div class="main-content">
					<div class="row">
						<div class="col-md-9">
							<!-- WIDGET NO HEADER -->
							<div class="widget widget-hide-header">
								<div class="widget-header hide">
									<h3>Summary Info</h3>
								</div>
								<div class="widget-content">
									<div class="row">
										<div class="col-md-3">
											<div class="easy-pie-chart green" data-percent="70">
												<span class="percent">70</span>
											</div>
											<p class="text-center">Task Completion</p>
										</div>
										<div class="col-md-3">
											<div class="easy-pie-chart red" data-percent="22">
												<span class="percent">22</span>
											</div>
											<p class="text-center">Overall Project Completion</p>
										</div>
										<div class="col-md-3">
											<div class="easy-pie-chart yellow" data-percent="65">
												<span class="percent">65</span>
											</div>
											<p class="text-center">Disk Space Used</p>
										</div>
										<div class="col-md-3">
											<div class="easy-pie-chart red" data-percent="87">
												<span class="percent">87</span>
											</div>
											<p class="text-center">Bandwidth Used</p>
										</div>
									</div>
								</div>
							</div>
							<!-- WIDGET NO HEADER -->
						
						</div>
					</div>
				</div>
						
 <div class="box-body">
        <div class="col-lg-3 col-xs-6">
          <div class="small-box bg-teal">
            <div class="inner">
              <h3>{{ ramAvail }}</h3>

              <p>RAM libre</p>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-xs-6">
          <!-- small box -->
          <div class="small-box bg-orange">
            <div class="inner">
              <h3>{{ ramTotal }}</h3>

              <p>RAM total</p>
            </div>
          </div>
        </div>
         <div class="col-lg-3 col-xs-6">
          <div class="small-box bg-maroon disabled">
            <div class="inner">
              <h3>{{ ramPerc }}</h3>
		
		<p>Porcentaje</p>
            </div>
          </div>
        </div>
          <!-- /.info-box -->
</div>
</section>
<section class="content">
        <div class="col-lg-3 col-xs-6">
          <div class="small-box bg-green">
            <div class="inner">
              <h3>{{ diskAvail }}</h3>

              <p>Memoria libre</p>
            </div>
           <div class="icon">
              <i class="ion ion-stats-bars"></i>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-xs-6">
 <!-- small box -->
          <div class="small-box bg-green">
            <div class="inner">
              <h3>{{ diskTotal }}</h3>

              <p>Memoria total</p>
            </div>
            <div class="icon">
              <i class="ion ion-stats-bars"></i>
            </div>
          </div>
</div>

</section>

 <section class="content">
                <p>
                        <a class="btn bg-maroon" href=" ">Icinga</a>
                        <a class="btn bg-purple" href=" ">Grafana</a>
                        <a class="btn bg-blue" href="stark">Resumen</a>
                </p>
</div>
</section>
</div>
%include('footer.tpl')
