class PageDashboard:
    def __init__(self,page):
        self.page = page
        self._dashboard_header =page.locator('//span[@class="oxd-topbar-header-breadcrumb"]')


    @property
    def dashboard_header(self):
        return self._dashboard_header