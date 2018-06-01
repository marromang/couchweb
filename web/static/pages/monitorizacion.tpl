%include('header.tpl')
<div class="content-wrapper">

<section class="content">
<section class="header">
<h3>Host: jarvis </h3>
</section>
 <div class="box-body">
        <div class="col-lg-3 col-xs-6">
          <div class="small-box bg-green">
            <div class="inner">
              <h3>{{ ramAvail }}</h3>

              <p>RAM libre</p>
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
              <h3>{{ ramTotal }}</h3>

              <p>RAM total</p>
            </div>
            <div class="icon">
              <i class="ion ion-stats-bars"></i>
            </div>
          </div>
        </div>
         <div class="col-lg-3 col-xs-6">
          <div class="small-box bg-green">
            <div class="inner">
              <h3>{{ ramPerc }}</h3>
            </div>
           <div class="icon">
              <i class="ion ion-stats-bars"></i>
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
