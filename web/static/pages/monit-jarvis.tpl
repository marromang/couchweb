%include('header.tpl')
<div class="content-wrapper">
  <section class="content">
    <section class="header">
      <h3>Host: jarvis </h3>
    </section>
    <div class="main-content">
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
      </div>

      <div class="box-body">
        <div class="col-lg-3 col-xs-6">
          <div class="small-box bg-teal">
            <div class="inner">
              <h3>{{ diskAvail }}</h3>
              <p>Memoria libre</p>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-xs-6">
          <div class="small-box bg-orange">
            <div class="inner">
              <h3>{{ diskTotal }}</h3>
              <p>Memoria total</p>
            </div>
          </div>
        </div>
      </div>
      <div class="box-body">
        <p>
          <a class="btn bg-purple" href="http://172.16.103.53/zabbix">Zabbix</a>
        </p>
      </div>
    </div>
  </section>
 </div>
%include('footer.tpl')

