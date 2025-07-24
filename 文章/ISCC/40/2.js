Java.perform(function() {
    // 监听 ActivityThread 的 handleLaunchActivity 方法
    var ActivityThread = Java.use("android.app.ActivityThread");
    
    ActivityThread.handleLaunchActivity.implementation = function(r, pendingActions, customIntent) {
        console.log("[+] 拦截到应用启动");
        
        // 获取 Intent 对象
        var intent = r.intent.value;
        
        // 获取当前的 component
        var component = intent.getComponent();
        
        if (component) {
            var componentName = component.getClassName();
            console.log("[+] 当前启动的组件：" + componentName);
            
            // 如果是 VideoActivity，替换为 MainActivity
            if (componentName === "com.example.ggad.VideoActivity") {
                console.log("[*] 正在将入口从 VideoActivity 修改为 MainActivity");
                
                // 创建新的 ComponentName
                var ComponentName = Java.use("android.content.ComponentName");
                var newComponent = ComponentName.$new("com.example.ggad", "com.example.ggad.MainActivity");
                
                // 替换 Intent 的 component
                intent.setComponent(newComponent);
                console.log("[+] 入口 Activity 已修改为 MainActivity");
            }
        }
        
        // 调用原始方法
        return this.handleLaunchActivity(r, pendingActions, customIntent);
    };
});
