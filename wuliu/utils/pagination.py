from django.utils.safestring import mark_safe

class Page:
    def __init__(self,current_page,data_count,per_page_count = 3,page_num = 7):
        self.current_page = current_page
        self.data_count = data_count
        self.per_page_count = per_page_count
        self.page_num = page_num

    def start(self):
        return (self.current_page-1) * self.per_page_count

    def end(self):
        return self.current_page * self.per_page_count

    @property
    def total_count(self):
        v,y = divmod(self.data_count,self.per_page_count)    #总数据 // 每页的数据   总数据  % 每页的数据
        if y:
            v += 1
        return v

    def page_str(self,base_url):
        page_list = []
        start_index = self.current_page - 5
        end_index = self.current_page + 6
        page_num = 11
        if self.total_count < self.page_num:
            start_index = 1
            end_index = self.total_count + 1
        else:
            if self.current_page <= (page_num+1) / 2:   #当当前页数小于这个+1的一半时 会导致出现-1的情况这是不允许的
                start_index = 1
                end_index = page_num + 1     #[1,12]        小的时候会出现这个情况    等[5,12]
            else:
                start_index = self.current_page - (page_num - 1)/2
                end_index = self.current_page + (page_num+1) / 2
                if (self.current_page + (page_num - 1)/2) > self.total_count:
                    end_index = self.total_count
                    start_index = self.total_count - page_num + 1

        if self.current_page == 1:
            prev = '<a class="page" href="javascript:void(0);">上一页</a>'
        else:
            prev = '<a class="page" href="%s?p=%s">上一页</a>'%(base_url,self.current_page-1)
        page_list.append(prev)

        for i in range(int(start_index),int(end_index)):
            if i == self.current_page:
                temp = '<a class="page active" href="%s?p=%s">%s</a>'%(base_url,i,i)
            else:
                temp = '<a class="page" href="%s?p=%s">%s</a>'%(base_url,i,i)
            page_list.append(temp)

        if self.current_page >= self.total_count:
            next = '<a class="page" href="javascript:void(0);">下一页</a>'
        else:
            next = '<a class="page" href="%s?p=%s">下一页</a>'%(base_url,self.total_count+1)
        page_list.append(next)

        jump = """
            <input id="input" type="input" type="text" placeholder="跳转请输入页数" />
            <a onclick="jumpTo(this,'%s?p=');" id="i1">Go</a>
            <script>
                function jumpTo(ths,base){
                    var val = ths.previousElementSibling.value;
                    location.href = base + val;
                }
            </script>
        """%(base_url)
        page_list.append(jump)
        page_str = ''.join(page_list)
        page_str = mark_safe(page_str)
        return page_str

